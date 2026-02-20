

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class QWASMJob:
    name: str
    payload: dict


def execute(job: QWASMJob) -> dict:
    """Deterministic placeholder execution: echo payload."""
    return {"job": job.name, "result": job.payload}
