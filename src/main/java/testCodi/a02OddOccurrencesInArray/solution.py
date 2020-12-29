# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from typing import List


def solution_odd_occurrences(A: List[int]) -> int:
    # write your code in Python 3.6
    candidates = []
    for item in A:
        if item in candidates:
            candidates.remove(item)
        else:
            candidates.append(item)
    return candidates[0]
