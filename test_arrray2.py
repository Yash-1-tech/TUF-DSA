# test_longest_subarray.py

import random
import pytest
from array2 import sliding_window_2ptrs 
# Import your function here
# from solution import sliding_window_2ptrs


def brute_force(arr, k):
    longest = []

    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == k:
                if (j - i + 1) > len(longest):
                    longest = arr[i:j+1]
            elif s > k:
                break       # valid because all numbers are positive

    return longest if longest else None


def test_random():
    for _ in range(10000):

        n = random.randint(1, 15)
        arr = [random.randint(1, 10) for _ in range(n)]
        k = random.randint(1, 25)

        expected = brute_force(arr, k)
        got = sliding_window_2ptrs(arr, k)

        assert got == expected, (
            f"\nArray: {arr}"
            f"\nk = {k}"
            f"\nExpected: {expected}"
            f"\nGot: {got}"
        )