"""Symplectic prime-shift operator sketches.

Placeholder scaffolding for "twistor shifts" / prime-shift inspired operators.
The only promise: clean interfaces + deterministic behavior when seeded.
"""

from __future__ import annotations
import numpy as np


def symplectic_shift_matrix(N: int, k: int = 1) -> np.ndarray:
    """Return a simple permutation-like shift matrix of size N with shift k."""
    k = int(k) % int(N)
    M = np.zeros((N, N), dtype=float)
    for i in range(N):
        M[i, (i + k) % N] = 1.0
    return M


def prime_weighted_shift(N: int, seed: int = 0) -> np.ndarray:
    """Toy 'prime-weighted' symmetric operator: shift + transpose with random weights."""
    rng = np.random.default_rng(seed)
    S = symplectic_shift_matrix(N, 1)
    w = rng.uniform(0.0, 1.0, size=N)
    W = np.diag(w)
    H = W @ S + (W @ S).T
    return (H + H.T) / 2.0
