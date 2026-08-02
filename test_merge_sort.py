import random
import pytest
from merge_sort import merge_sort

@pytest.mark.parametrize("arr",[
    [],
    [1],
    [2,1],
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
    result = merge_sort(arr.copy())
    assert result == expected

def test_random_list():
    for _ in range(1000):
        arr = [random.randint(-100,100) for _ in range(random.randint(0,50))]
        assert merge_sort(arr.copy()) == sorted(arr)

def test_duplicate():
    for i in range(10):
        arr = [i] * 100
        assert merge_sort(arr.copy()) == sorted(arr)
