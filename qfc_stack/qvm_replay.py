"""Deterministic replay layer."""

from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class ReplayResult:
    ok: bool
    message: str


def save_trace_npz(path: str, **arrays) -> None:
    fixed = {k: np.asarray(v) for k, v in arrays.items()}
    np.savez(path, **fixed)


def load_trace_npz(path: str) -> dict[str, np.ndarray]:
    with np.load(path) as z:
        return {k: z[k] for k in z.files}


def compare_arrays(a: np.ndarray, b: np.ndarray, atol: float = 1e-10) -> ReplayResult:
    if a.shape != b.shape:
        return ReplayResult(False, f"shape mismatch: {a.shape} vs {b.shape}")
    if not np.allclose(a, b, atol=atol, rtol=0.0):
        return ReplayResult(False, "array mismatch (not allclose)")
    return ReplayResult(True, "ok")
