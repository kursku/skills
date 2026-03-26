"""Tests for catalog.py — classification, frontmatter parsing, quality checks."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from catalog import parse_frontmatter, classify, quality_issues


# ── Frontmatter parsing ──────────────────────────────────────────────────────

def test_parse_basic_frontmatter(tmp_path):
    p = tmp_path / "SKILL.md"
    p.write_text("---\nname: my-skill\ndescription: A test skill for testing\nrisk: safe\n---\n# Content")
    fm = parse_frontmatter(p)
    assert fm["name"] == "my-skill"
    assert fm["description"] == "A test skill for testing"
    assert fm["risk"] == "safe"


def test_parse_quoted_values(tmp_path):
    p = tmp_path / "SKILL.md"
    p.write_text('---\nname: "quoted-skill"\ndescription: \'single quoted\'\n---\n# Content')
    fm = parse_frontmatter(p)
    assert fm["name"] == "quoted-skill"
    assert fm["description"] == "single quoted"


def test_parse_missing_frontmatter(tmp_path):
    p = tmp_path / "SKILL.md"
    p.write_text("# No frontmatter here\nJust content.")
    fm = parse_frontmatter(p)
    assert fm == {} or fm.get("name") is None


# ── Classification ───────────────────────────────────────────────────────────

def test_classify_security():
    cat = classify("pentest-checklist", "Penetration testing checklist", [])
    assert cat == "security"


def test_classify_frontend():
    cat = classify("react-patterns", "Modern React UI patterns", ["react", "frontend"])
    assert cat == "frontend"


def test_classify_backend():
    cat = classify("fastapi-pro", "Build FastAPI applications", ["python", "api"])
    assert cat == "backend"


def test_classify_content():
    cat = classify("marketing-ideas", "Provide marketing strategies", ["marketing"])
    assert cat in ("business", "content")


def test_classify_ai_agents():
    cat = classify("crewai", "Multi-agent framework for AI", ["llm", "agents"])
    assert cat == "ai-agents"


# ── Quality issues ───────────────────────────────────────────────────────────

def test_quality_no_issues():
    fm = {"name": "good-skill", "description": "A well-described skill for production use", "risk": "safe"}
    issues = quality_issues(fm)
    assert issues == []


def test_quality_missing_name():
    fm = {"description": "Has description but no name", "risk": "safe"}
    issues = quality_issues(fm)
    assert "missing-name" in issues


def test_quality_short_description():
    fm = {"name": "short", "description": "Too short", "risk": "safe"}
    issues = quality_issues(fm)
    assert "description-too-short" in issues


def test_quality_risk_unset():
    fm = {"name": "no-risk", "description": "A skill without risk classification set"}
    issues = quality_issues(fm)
    assert "risk-unset" in issues


def test_quality_risk_unknown():
    fm = {"name": "unknown-risk", "description": "A skill with unknown risk level", "risk": "unknown"}
    issues = quality_issues(fm)
    assert "risk-unset" in issues


def test_quality_risk_none_is_valid():
    fm = {"name": "none-risk", "description": "A pure text reasoning skill here", "risk": "none"}
    issues = quality_issues(fm)
    assert "risk-unset" not in issues


def test_quality_stub_content():
    fm = {"name": "stub", "description": "A stub skill with no real content", "risk": "safe", "quality": "stub"}
    issues = quality_issues(fm)
    assert "stub-content" in issues


def test_quality_generic_description():
    fm = {"name": "seo", "description": "Seo — skill especializada para seo", "risk": "safe"}
    issues = quality_issues(fm)
    assert "description-generic" in issues


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
