import pandas as pd
from df_sample import dict_to_df
from pandas.testing import assert_frame_equal


def test_df_sample():
    test_dict = {"a": [1, 2, 3], "b": [4, 5, 6]}
    actual_df = pd.DataFrame(test_dict)
    assert_frame_equal(actual_df, dict_to_df(test_dict))
