import pytest
from random import randint as r
from two_sum import dict_2sum


def brute_force(arr, k):
    answers = set()

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                answers.add(tuple(sorted((arr[i], arr[j]))))

    if answers:
        return True, answers
    return False, set()


def test_random():
    for _ in range(10000):
        n = r(1, 15)
        arr = [r(1, 10) for _ in range(n)]
        k = r(1, 25)

        expected_found, expected_pairs = brute_force(arr, k)
        got = dict_2sum(arr, k)

        if not expected_found:
            assert got == False, (
                f"\nArray: {arr}"
                f"\nk = {k}"
                f"\nExpected: False"
                f"\nGot: {got}"
            )
        else:
            assert got[0] == True, (
                f"\nArray: {arr}"
                f"\nk = {k}"
                f"\nExpected one of: {expected_pairs}"
                f"\nGot: {got}"
            )

            pair = tuple(sorted((got[1], got[2])))

            assert pair in expected_pairs, (
                f"\nArray: {arr}"
                f"\nk = {k}"
                f"\nExpected one of: {expected_pairs}"
                f"\nGot: {pair}"
            )
