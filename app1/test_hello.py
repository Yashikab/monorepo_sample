from hello import sum_iteration


def test_sum_iteration():
    assert sum_iteration(10) == 55
    assert sum_iteration(9) == 45
