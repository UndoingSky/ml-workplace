import numpy as np


def main() -> None:
    """Small demo of NumPy shapes, slicing, and broadcasting."""

    arr1 = np.array([1, 2, 3, 4])  # 1D array
    arr2 = np.array(
        [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    )  # 2D array

    arr3 = np.array(
        [
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
            [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
        ]
    )

    print(arr1.ndim)
    print(arr2.ndim)

    sum_val = arr3[0, 0, 0] + arr3[1, 2, 3]
    print(sum_val)

    slicing = np.array(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    )

    print(slicing[:2, 2:])

    table1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    table2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

    print(table1.shape)
    print(table2.shape)

    multiplication_table = table1 * table2

    print(multiplication_table)

    rng = np.random.default_rng()
    print(rng.integers(0, 7))


if __name__ == "__main__":
    main()