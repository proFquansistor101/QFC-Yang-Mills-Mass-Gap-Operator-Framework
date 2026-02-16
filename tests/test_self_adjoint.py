import numpy as np
from toy_models.spectral_gap_toy import build_operator


def test_operator_is_symmetric():
    rng = np.random.default_rng(0)
    H = build_operator(N=32, lam=0.2, rng=rng)
    assert np.allclose(H, H.T)
