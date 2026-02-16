import numpy as np
from toy_models.twistor_shifts import symplectic_shift_matrix


def test_shift_matrix_is_permutation_like():
    N = 16
    S = symplectic_shift_matrix(N, 3)
    assert np.allclose(S.sum(axis=1), 1.0)
    assert np.allclose(S.sum(axis=0), 1.0)
