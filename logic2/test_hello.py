from module import generate_df
from hello import double_element_for_dict

def test_generate_df():
    target = {"a": [1, 2]}
    actual_df = generate_df(target)
    assert actual_df["a"][0] == 1
    assert actual_df["a"][1] == 2

def test_double_df():
    target = {"a": [1, 2]}
    actual_df = double_element_for_dict(target)
    assert actual_df["a"][0] == 2
    assert actual_df["a"][1] == 4
