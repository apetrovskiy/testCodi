# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# from typing import List


def solution_tape_equilibrium(A):
    # write your code in Python 3.6
    #     return min([calculate_diff(A, i) for i in range(1, len(A))])
    sum_left = A[0]
    sum_right = sum(A[1:])
    best_result = abs(sum_left - sum_right)
    # print(f"init sum left = {sum_left},
    # init sum right = {sum_right}, init best = {best_result}")
    for index in range(1, len(A) - 1):
        sum_right -= A[index]
        sum_left += A[index]
        current_result = abs(sum_left - sum_right)
        best_result = current_result \
            if current_result < best_result else best_result
        # print(f"sum left = {sum_left},
        # sum right = {sum_right}, best = {best_result}")
    return best_result

# def calculate_diff(array: List[int], index: int) -> int:
#     return abs(sum(array[:index]) - sum(array[index:]))
