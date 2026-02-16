"""Multi-resolution confinement penalty placeholder for SMRK-style constraints."""

from __future__ import annotations
import numpy as np


def confinement_penalty(signal: np.ndarray, scales: int = 4) -> float:
    """Compute a simple multi-scale roughness penalty."""
    x = np.asarray(signal, dtype=float)
    if x.size < 2:
        return 0.0
    penalty = 0.0
    cur = x.copy()
    for _ in range(int(scales)):
        penalty += float(np.mean(np.abs(np.diff(cur))))
        if cur.size >= 4:
            cur = 0.5 * (cur[::2] + cur[1::2])
        else:
            break
    return penalty
