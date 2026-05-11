"""End-to-end UX evaluation that runs every heuristic and aggregates."""

from dataclasses import dataclass, field

from .heuristics import (
    HeuristicScore,
    score_predictability,
    score_recoverability,
    score_transparency,
    score_trust,
)


@dataclass
class UXEvaluation:
    overall: float
    band: str
    scores: list[HeuristicScore] = field(default_factory=list)
    weakest: str | None = None
    strongest: str | None = None


def _overall_band(score: float) -> str:
    if score >= 80:
        return "ship-ready"
    if score >= 60:
        return "polish-needed"
    if score >= 40:
        return "iterate"
    return "rework"


def evaluate(
    description: str,
    *,
    shows_sources: bool = False,
    shows_confidence: bool = False,
    has_undo: bool = False,
    has_edit: bool = False,
    deterministic: bool = False,
    shows_steps: bool = False,
    has_attribution: bool = False,
    has_guardrails: bool = False,
) -> UXEvaluation:
    """Run all four heuristics and produce a single evaluation object."""
    scores = [
        score_transparency(
            description,
            shows_sources=shows_sources,
            shows_confidence=shows_confidence,
        ),
        score_recoverability(description, has_undo=has_undo, has_edit=has_edit),
        score_predictability(
            description,
            deterministic=deterministic,
            shows_steps=shows_steps,
        ),
        score_trust(
            description,
            has_attribution=has_attribution,
            has_guardrails=has_guardrails,
        ),
    ]
    overall = round(sum(s.score for s in scores) / len(scores), 2)
    weakest = min(scores, key=lambda s: s.score).name
    strongest = max(scores, key=lambda s: s.score).name
    return UXEvaluation(
        overall=overall,
        band=_overall_band(overall),
        scores=scores,
        weakest=weakest,
        strongest=strongest,
    )
