"""Spectral gap toy model (Δ(λ)).

This file intentionally stays lightweight:
- Construct a simple symmetric matrix operator depending on λ
- Compute eigenvalues and a naive spectral gap estimate
- Return a trace suitable for deterministic replay

The goal is not physics accuracy, but a reproducible scaffold.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class DeltaLambdaTrace:
    seed: int
    N: int
    lam: float
    eigenvalues: np.ndarray

    def to_dict(self) -> dict:
        return {
            "seed": int(self.seed),
            "N": int(self.N),
            "lam": float(self.lam),
            "eigenvalues": self.eigenvalues.astype(float).tolist(),
        }


def build_operator(N: int, lam: float, rng: np.random.Generator) -> np.ndarray:
    """Build a symmetric toy operator H(λ)."""
    A = rng.normal(0.0, 0.05, size=(N, N))
    H = (A + A.T) / 2.0
    H += lam * np.diag(np.arange(N, dtype=float))
    return H


def run_delta_lambda(N: int = 64, lam: float = 0.1, seed: int = 42) -> tuple[float, DeltaLambdaTrace]:
    """Run the Δ(λ) toy experiment and return (gap, trace)."""
    rng = np.random.default_rng(seed)
    H = build_operator(N=N, lam=lam, rng=rng)
    evals = np.linalg.eigvalsh(H)
    gap = float(evals[1] - evals[0]) if len(evals) >= 2 else 0.0
    trace = DeltaLambdaTrace(seed=seed, N=N, lam=lam, eigenvalues=evals)
    return gap, trace
