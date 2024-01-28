import numpy as np


def sum_iteration(itr_num: int) -> int:
    return np.sum([i for i in range(1, itr_num + 1)])


def main() -> None:
    total = sum_iteration(10)
    print(total)


if __name__ == "__main__":
    main()
