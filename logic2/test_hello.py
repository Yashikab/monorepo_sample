from logic2.hello import generate_df


def test_generate_df():
    target = {"a": [1, 2]}
    actual_df = generate_df(target)
    assert actual_df["a"][0] == 1
    assert actual_df["a"][1] == 2
