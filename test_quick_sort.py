import random
import pytest
from quick_sort import quick_sort


@pytest.mark.parametrize("arr", [
    [],
    [1],
    [2, 1],
    [1, 2],
    [3, 2, 1],
    [1, 2, 3],
    [5, 4, 3, 2, 1],
    [4, 2, 3, 4, 5, 5, 1, 2, 5, 7, 3, 4, 2],
    [4, 4, 4, 4],
    [2, 1, 2, 1, 2],
    [3, 3, 1, 2, 3],
    [-1, 5, -3, 2, 0],
])

def test_fixed_cases(arr):
    expected = sorted(arr)
    result = quick_sort(arr.copy())
    assert result == expected


def test_random_arrays():
    for _ in range(1000):
        arr = [random.randint(-100, 100) for _ in range(random.randint(0, 50))]
        expected = sorted(arr)
        result = quick_sort(arr.copy())
        if result != expected:
            print(arr)
            print()
            print()
            print(expected)
            print()
            print()
            print(result)
        assert result == expected


def test_large_random_array():
    arr = [random.randint(-10000, 10000) for _ in range(5000)]
    expected = sorted(arr)
    result = quick_sort(arr.copy())
    if result != expected:
                print(arr)
                print()
                print()
                print(expected)
                print()
                print()
                print(result)
    assert result == expected


def test_duplicates():
    arr = [5] * 100
    assert quick_sort(arr.copy()) == sorted(arr)


def test_already_sorted():
    arr = list(range(100))
    assert quick_sort(arr.copy()) == arr


def test_reverse_sorted():
    arr = list(range(100, 0, -1))
    assert quick_sort(arr.copy()) == sorted(arr)


def test_in_place_behavior():
    arr = [4, 2, 1, 3]
    returned = quick_sort(arr)

    # quick() should sort the original list
    assert arr == [1, 2, 3, 4]

    # and return the same list object
    assert returned is arr
