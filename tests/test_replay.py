from toy_models.spectral_gap_toy import run_delta_lambda
from qfc_stack.qvm_replay import compare_arrays


def test_replay_delta_lambda_eigenvalues():
    gap1, trace1 = run_delta_lambda(N=32, lam=0.15, seed=123)
    gap2, trace2 = run_delta_lambda(N=32, lam=0.15, seed=123)
    assert gap1 == gap2
    res = compare_arrays(trace1.eigenvalues, trace2.eigenvalues)
    assert res.ok, res.message
