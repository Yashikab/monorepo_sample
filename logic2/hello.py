from typing import Dict

import pandas as pd


def generate_df(data: Dict[str, list]):
    return pd.DataFrame(data)


if __name__ == "__main__":
    print(generate_df({"a": [1, 2], "b": [3, 4]}))
