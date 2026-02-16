"""Wilson lattice scaffolding.

This module provides a minimal placeholder for SU(2)/SU(3)-like Wilson action loops.
It does NOT implement full group integration; it only defines data structures and
deterministic trace generation for later replacement.
"""

from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class LatticeTrace:
    seed: int
    volume: tuple[int, int, int, int]
    beta: float
    plaquette_mean: float

    def to_dict(self) -> dict:
        return {
            "seed": int(self.seed),
            "volume": [int(x) for x in self.volume],
            "beta": float(self.beta),
            "plaquette_mean": float(self.plaquette_mean),
        }


def run_wilson_placeholder(volume=(8, 8, 8, 8), beta: float = 6.0, seed: int = 1) -> tuple[float, LatticeTrace]:
    """Generate a deterministic placeholder observable: mean 'plaquette'."""
    rng = np.random.default_rng(seed)
    base = 0.55 + 0.01 * np.tanh((beta - 5.5))
    plaquettes = rng.normal(loc=base, scale=0.02, size=256)
    plaquette_mean = float(np.mean(plaquettes))
    action = float(-beta * plaquette_mean)
    return action, LatticeTrace(seed=seed, volume=tuple(volume), beta=beta, plaquette_mean=plaquette_mean)
