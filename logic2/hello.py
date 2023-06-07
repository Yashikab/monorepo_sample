import module

def double_element_for_dict(target: dict):
    df = module.generate_df(target)
    return df * 2

if __name__ == "__main__":
    print(module.generate_df({"a": [1, 2], "b": [3, 4]}))
    print(double_element_for_dict({"a": [1, 2], "b": [3, 4]}))
