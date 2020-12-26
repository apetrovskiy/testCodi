# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
    shift = K % len(A)
    if shift == 0:
        return A
    result = []
    result.extend(A[len(A) - shift:])
    result.extend(A[:-shift])
    A[len(A) - shift:].extend(A[:-shift])
    return result
