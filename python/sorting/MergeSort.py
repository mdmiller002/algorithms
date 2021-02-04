
from typing import List
import logging

logging.basicConfig(level=logging.ERROR, format="%(message)s")

def merge_sort(arr: List):
  logging.debug(f"arr: {arr}")
  if (arr is None or len(arr) <= 1):
    return
  middle = len(arr) // 2
  left = arr[:middle]
  right = arr[middle:]
  logging.debug(f"left: {left}")
  logging.debug(f"right: {right}")
  logging.debug("================")
  merge_sort(left)
  merge_sort(right)
  _merge(left, right, arr)

def _merge(left: List, right: List, arr: List):
  logging.debug(f"Merging {left} with {right} into {arr}")
  i = 0
  j = 0
  k = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    k += 1

  while i < len(left):
    arr[k] = left[i]
    k += 1
    i += 1
  while j < len(right):
    arr[k] = right[j]
    k += 1
    j += 1
  return arr

if __name__ == '__main__':
  a = [9, 4, 3, 6, 9, 7]
  merge_sort(a)
  print(a)

