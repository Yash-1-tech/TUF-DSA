from random import randint as r
import pytest
from sort_012 import sort_012

def test_random():
    for _ in range(10000):
        arr = [r(0,2) for _ in range(r(0,50))]
        expected = sorted(arr)
        barr = arr.copy()
        sort_012(barr)
        if barr != expected:
            print(arr)
            print(barr)
        assert barr == expected
