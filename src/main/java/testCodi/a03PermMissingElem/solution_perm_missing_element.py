# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_perm_missing_element(A):
    # write your code in Python 3.6
    # zero or one elements
    if len(A) == 0:
        return 1
    A.sort()
    # the first item
    if A[0] != 1:
        return 1
    # the last item
    if A[len(A) - 1] != len(A) + 1:
        return len(A) + 1
    for index in range(1, len(A) + 1):
        if index < A[index - 1]:
            return A[index - 1] - 1
    return 0
