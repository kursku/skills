"""Tests for infer_risk.py — risk inference logic."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from infer_risk import infer_risk, extract_frontmatter, set_risk_in_frontmatter, get_existing_risk


# ── Risk inference ───────────────────────────────────────────────────────────

def test_offensive_pentest():
    risk = infer_risk("pentest-tool", "Penetration testing framework", "Run exploits against target", Path("."))
    assert risk == "offensive"


def test_offensive_metasploit():
    risk = infer_risk("metasploit-framework", "Metasploit usage guide", "Use msfconsole to launch exploits", Path("."))
    assert risk == "offensive"


def test_offensive_reverse_shell():
    risk = infer_risk("shells", "Shell management", "Generate reverse shell payloads", Path("."))
    assert risk == "offensive"


def test_critical_deploy():
    risk = infer_risk("deploy-tool", "Deploy applications to production", "Runs deployment pipeline to AWS", Path("."))
    assert risk == "critical"


def test_critical_credentials():
    risk = infer_risk("secret-manager", "Credential management system", "Manages API keys and secrets in vault", Path("."))
    assert risk == "critical"


def test_critical_whatsapp_api():
    risk = infer_risk("whatsapp-integration", "WhatsApp Cloud API integration", "Send messages via WhatsApp API", Path("."))
    assert risk == "critical"


def test_safe_marketing_content():
    """Marketing/content skills should NOT be critical."""
    risk = infer_risk("content-calendar", "Plan your content calendar", "Create a monthly content strategy", Path("."))
    assert risk in ("safe", "none"), f"Expected safe/none but got {risk}"


def test_safe_seo_strategy():
    """SEO strategy skills should NOT be critical."""
    risk = infer_risk("seo-audit", "SEO audit checklist", "Review your site for SEO best practices", Path("."))
    assert risk in ("safe", "none"), f"Expected safe/none but got {risk}"


def test_safe_copywriting():
    """Copywriting skills should NOT be critical."""
    risk = infer_risk("ad-copy", "Write ad copy variants", "Create compelling headlines and body copy", Path("."))
    assert risk in ("safe", "none"), f"Expected safe/none but got {risk}"


def test_safe_pricing_strategy():
    """Pricing strategy should NOT be critical."""
    risk = infer_risk("pricing-guide", "Agency pricing guide", "Set your prices and packages", Path("."))
    assert risk in ("safe", "none"), f"Expected safe/none but got {risk}"


def test_safe_analytics_not_critical():
    """Analytics skills that just analyze data should be safe."""
    risk = infer_risk("analytics-dashboard", "Build analytics dashboards", "Visualize your marketing metrics", Path("."))
    assert risk in ("safe", "none"), f"Expected safe/none but got {risk}"


def test_safe_template():
    """Template/framework skills should be safe."""
    risk = infer_risk("email-template", "HTML email template builder", "Design responsive email templates", Path("."))
    assert risk in ("safe", "none"), f"Expected safe/none but got {risk}"


# ── Frontmatter manipulation ────────────────────────────────────────────────

def test_extract_frontmatter():
    content = "---\nname: test\ndescription: A test\n---\n# Body"
    fm = extract_frontmatter(content)
    assert fm["name"] == "test"
    assert fm["description"] == "A test"


def test_get_existing_risk():
    content = "---\nname: test\nrisk: critical\n---\n# Body"
    assert get_existing_risk(content) == "critical"


def test_get_existing_risk_none():
    content = "---\nname: test\n---\n# Body"
    assert get_existing_risk(content) is None


def test_set_risk_new():
    content = "---\nname: test\n---\n# Body"
    result = set_risk_in_frontmatter(content, "safe")
    assert "risk: safe" in result


def test_set_risk_replace():
    content = "---\nname: test\nrisk: unknown\n---\n# Body"
    result = set_risk_in_frontmatter(content, "critical")
    assert "risk: critical" in result
    assert "risk: unknown" not in result


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
