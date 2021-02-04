import random
from typing import List
from sorting.MergeSort import merge_sort

def test_null_input():
  a = None
  merge_sort(a)
  assert a is None

def test_empty_input():
  a = []
  merge_sort(a)
  assert a == []

def test_simple():
  _execute_sort([4, 2, 7, 3, 1, 8])

def test_sorted():
  _execute_sort([1, 2, 3, 4, 5])

def test_negatives():
  _execute_sort([-4, -9, -12, -29])

def test_negatives_and_positives():
  _execute_sort([5, 10, -39, 14, 3, -5, 0, -8])

def test_duplicates():
  _execute_sort([3, 3, 3])

def test_multiple_duplicates():
  _execute_sort([-2, -2, 0, 0, 5, 5])

def test_zeros():
  _execute_sort([0, 0, 0])

def test_single_element():
  _execute_sort([1])

def test_merge_sort_generative():
  for _ in range(100):
    arr = gen_random_array()
    _execute_sort(arr, False)

def gen_random_array():
  min_int = -2 ** 63
  max_int = 2 ** 63 - 1
  size = random.randrange(5, 1_000)
  return [random.randint(min_int, max_int) for i in range(size)]

def _execute_sort(arr: List, display=True):
  expected = sorted(arr)
  merge_sort(arr)
  assert arr == expected