import numpy as np
from qfc_stack.smrk_probe import spectral_invariants


def test_spectral_invariants_basic():
    ev = np.array([1.0, 2.0, 3.0])
    inv = spectral_invariants(ev)
    assert inv["count"] == 3
    assert np.isclose(inv["mean"], 2.0)
