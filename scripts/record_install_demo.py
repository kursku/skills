#!/usr/bin/env python3
"""
record_install_demo.py
======================
Records a GIF of the skill install flow at claude.ai/customize/skills.

Requirements:
  pip install playwright && python -m playwright install chromium
  ffmpeg must be on PATH

Usage:
  python scripts/record_install_demo.py [--skill path/to/file.skill]

The script uses your existing Chrome profile so you stay logged in.
Close Chrome before running.
"""

import asyncio
import subprocess
import argparse
import shutil
import zipfile
import tempfile
from pathlib import Path
from playwright.async_api import async_playwright

# ── Config ────────────────────────────────────────────────────────────────────
CHROME_PROFILE = Path(r"C:\Users\nicol\AppData\Local\Microsoft\Edge\User Data")
VIDEO_DIR      = Path("dist/demo-recording")
OUTPUT_GIF     = Path("docs/assets/install-demo.gif")
VIEWPORT       = {"width": 1280, "height": 800}
TARGET_URL     = "https://claude.ai/customize/skills"

# GIF palette filter — high quality, reasonable size
FFMPEG_FILTER  = (
    "fps=12,scale=960:-1:flags=lanczos,"
    "split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer"
)

# ── Helpers ───────────────────────────────────────────────────────────────────

def build_demo_skill(dest_dir: Path) -> Path:
    """Create a minimal .skill file to use in the demo if none supplied."""
    skill_md = """\
---
name: demo-skill
description: "Demo skill for install walkthrough. Safe to delete after."
---

# Demo Skill

This is a placeholder skill used to demonstrate the install flow.
"""
    skill_dir = dest_dir / "demo-skill"
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(skill_md)

    zip_path = dest_dir / "demo-skill.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.write(skill_dir / "SKILL.md", "SKILL.md")

    skill_path = dest_dir / "demo-skill.skill"
    zip_path.rename(skill_path)
    shutil.rmtree(skill_dir)
    return skill_path


def video_to_gif(video_path: Path, gif_path: Path) -> None:
    gif_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path),
        "-vf", FFMPEG_FILTER,
        "-loop", "0",
        str(gif_path),
    ]
    print(f"\nffmpeg: {' '.join(cmd)}\n")
    subprocess.run(cmd, check=True)


# ── Main flow ─────────────────────────────────────────────────────────────────

async def record(skill_path: Path) -> None:
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        print("Launching Chrome with your profile (close Chrome first if open)...")
        ctx = await p.chromium.launch_persistent_context(
            user_data_dir=str(CHROME_PROFILE),
            channel="msedge",
            headless=False,
            viewport=VIEWPORT,
            record_video_dir=str(VIDEO_DIR),
            record_video_size=VIEWPORT,
            args=["--start-maximized"],
            slow_mo=400,           # slight slow-mo so the GIF is readable
        )

        page = ctx.pages[0] if ctx.pages else await ctx.new_page()

        # ── Step 1: land on the skills page ──────────────────────────────────
        print(f"Navigating to {TARGET_URL} ...")
        await page.goto(TARGET_URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(2000)

        # ── Step 2: find the "Add skill" / upload button ──────────────────────
        # Claude.ai may label this differently — try a few selectors
        upload_selectors = [
            "text=Add skill",
            "text=Upload skill",
            "text=Add",
            "[data-testid*='upload']",
            "button:has-text('skill')",
        ]
        upload_btn = None
        for sel in upload_selectors:
            try:
                upload_btn = page.locator(sel).first
                await upload_btn.wait_for(timeout=3000, state="visible")
                print(f"Found upload button via: {sel}")
                break
            except Exception:
                upload_btn = None

        if upload_btn is None:
            print(
                "WARNING: Could not find 'Add skill' button automatically.\n"
                "   The page may have changed. Please click it manually and\n"
                "   close the browser when done -- the video will still be saved."
            )
            await page.wait_for_timeout(30_000)  # wait up to 30 s for manual action
        else:
            await upload_btn.scroll_into_view_if_needed()
            await page.wait_for_timeout(600)
            await upload_btn.hover()
            await page.wait_for_timeout(600)

            # ── Step 3: handle the file chooser ──────────────────────────────
            async with page.expect_file_chooser() as fc_info:
                await upload_btn.click()
            file_chooser = await fc_info.value
            await file_chooser.set_files(str(skill_path))
            print(f"Uploaded: {skill_path.name}")
            await page.wait_for_timeout(3000)  # wait for success state

        # ── Done — close and let video flush ─────────────────────────────────
        await ctx.close()

    # ── Convert video → GIF ───────────────────────────────────────────────────
    videos = sorted(VIDEO_DIR.glob("*.webm"), key=lambda f: f.stat().st_mtime, reverse=True)
    if not videos:
        print("No .webm video found in dist/demo-recording/ — nothing to convert.")
        return

    latest = videos[0]
    print(f"\nVideo saved: {latest}")
    video_to_gif(latest, OUTPUT_GIF)
    print(f"\nGIF saved to {OUTPUT_GIF}")
    print(f"    Add it to your README with:")
    print(f'    ![Install demo]({OUTPUT_GIF})')


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Record skill install demo GIF")
    parser.add_argument(
        "--skill",
        type=Path,
        default=None,
        help="Path to a .skill file to upload in the demo. A minimal one is created if omitted.",
    )
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as tmp:
        if args.skill:
            skill_path = args.skill.resolve()
        else:
            skill_path = build_demo_skill(Path(tmp))
            print(f"Using generated demo skill: {skill_path}")

        asyncio.run(record(skill_path))


if __name__ == "__main__":
    main()
