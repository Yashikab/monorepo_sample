from hello import double_element_for_dict

def test_double_df():
    target = {"a": [1, 2]}
    actual_df = double_element_for_dict(target)
    assert actual_df["a"][0] == 2
    assert actual_df["a"][1] == 4
