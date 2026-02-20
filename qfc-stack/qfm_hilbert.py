

from __future__ import annotations
import numpy as np


def conformal_weight(N: int, alpha: float = 1.0) -> np.ndarray:
    """Return weight vector w_n = (n)^(-alpha)."""
    n = np.arange(1, int(N) + 1, dtype=float)
    return n ** (-float(alpha))


def weighted_inner(x: np.ndarray, y: np.ndarray, w: np.ndarray) -> float:
    """Weighted ℓ² inner product <x,y>_w = sum conj(x_i) y_i w_i."""
    x = np.asarray(x)
    y = np.asarray(y)
    w = np.asarray(w, dtype=float)
    return float(np.vdot(x, y * w).real)
