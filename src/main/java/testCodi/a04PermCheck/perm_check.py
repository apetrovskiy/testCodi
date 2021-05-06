# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    min_value = A[0]
    max_value = A[len(A) - 1]
    if len(A) != len(set(A)):
        return 0
    if min_value != 1:
        return 0
    if max_value != len(A):
        return 0
    return 1
