import pandas as pd


def dict_to_df(target_dict: dict) -> pd.DataFrame:
    df = pd.DataFrame(target_dict)
    return df


def main() -> None:
    result = dict_to_df({"a": [1, 2, 3], "b": [3, 4, 5]})
    print(result)


if __name__ == "__main__":
    main()
