import pytest
from simple import bubble_sort

def test_empty_list():
    assert bubble_sort([]) == []

def test_sort():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sorted_duplicates():
    assert bubble_sort([5, 4, 3, 3, 1]) == [1, 3, 3, 4, 5]

