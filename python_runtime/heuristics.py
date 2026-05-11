"""Heuristic scoring functions for AI-product UX.

Each heuristic returns a 0-100 score with a short rationale. Inputs
are simple feature descriptions (free text plus structured signals);
the heuristics are deliberately lightweight so they can run in any
agent harness without external dependencies.
"""

from dataclasses import dataclass


@dataclass
class HeuristicScore:
    name: str
    score: float
    rationale: str


def _band(score: float) -> str:
    if score >= 80:
        return "strong"
    if score >= 60:
        return "acceptable"
    if score >= 40:
        return "weak"
    return "missing"


def score_transparency(description: str, *, shows_sources: bool = False,
                       shows_confidence: bool = False) -> HeuristicScore:
    """How clearly does the experience expose what the AI did and why?"""
    text = description.lower()
    base = 30.0
    if "explain" in text or "why" in text or "because" in text:
        base += 20
    if shows_sources:
        base += 25
    if shows_confidence:
        base += 25
    score = round(min(100.0, base), 2)
    return HeuristicScore(
        name="transparency",
        score=score,
        rationale=f"transparency band: {_band(score)} (sources={shows_sources}, confidence={shows_confidence})",
    )


def score_recoverability(description: str, *, has_undo: bool = False,
                         has_edit: bool = False) -> HeuristicScore:
    """Can the user recover gracefully when the AI is wrong?"""
    text = description.lower()
    base = 25.0
    if "undo" in text or has_undo:
        base += 30
    if "edit" in text or has_edit:
        base += 25
    if "retry" in text or "regenerate" in text:
        base += 20
    score = round(min(100.0, base), 2)
    return HeuristicScore(
        name="recoverability",
        score=score,
        rationale=f"recoverability band: {_band(score)}",
    )


def score_predictability(description: str, *, deterministic: bool = False,
                         shows_steps: bool = False) -> HeuristicScore:
    """Can the user anticipate what the AI will do next?"""
    text = description.lower()
    base = 30.0
    if shows_steps or "steps" in text or "plan" in text:
        base += 30
    if deterministic:
        base += 25
    if "preview" in text or "dry-run" in text:
        base += 15
    score = round(min(100.0, base), 2)
    return HeuristicScore(
        name="predictability",
        score=score,
        rationale=f"predictability band: {_band(score)}",
    )


def score_trust(description: str, *, has_attribution: bool = False,
                has_guardrails: bool = False) -> HeuristicScore:
    """How well does the experience build appropriate user trust?"""
    text = description.lower()
    base = 30.0
    if has_attribution or "source" in text or "cited" in text:
        base += 25
    if has_guardrails or "safety" in text or "guardrail" in text:
        base += 25
    if "feedback" in text or "thumbs" in text or "rating" in text:
        base += 20
    score = round(min(100.0, base), 2)
    return HeuristicScore(
        name="trust",
        score=score,
        rationale=f"trust band: {_band(score)}",
    )
