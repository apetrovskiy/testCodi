# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from typing import List


def solution(A: List[int]) -> int:
    # write your code in Python 3.6
    '''
    candidates = []
    for item in A:
        if item in candidates:
            candidates.remove(item)
        else:
            candidates.append(item)
    return candidates[0]
    '''
    '''
    half_length = int(len(A) / 2)
    first_half_sum = 0
    second_half_sum = 0
    for index in range(0, half_length):
        first_half_sum += A[index]
    for index in range(half_length, len(A)):
        second_half_sum += A[index]
    return abs(first_half_sum - second_half_sum)
    '''
    A.sort()
    first_half_sum = 0
    second_half_sum = 0
    for index in range(0, len(A), 2):
        first_half_sum += A[index]
        if index + 1 < len(A):
            second_half_sum += A[index + 1]
    return abs(first_half_sum - second_half_sum)
