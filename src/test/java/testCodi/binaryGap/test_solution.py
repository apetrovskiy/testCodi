# [1..2,147,483,647].
from src.main.java.testCodi.binaryGap.solution import solution
import pytest

# from nose.tools import assert_equal

# import unittest
# from unittest import TestCase
# from parameterized import parameterized
# import parameterized
# from parameterized import parameterized, parameterized_class


# unittest
# class SolutionTest(TestCase):
# @parameterized.expand(
#     [9, 2], [529, 4], [20, 1], [1041, 5], [15, 0], [32, 0], [1, 0], [5, 1],
#     [2147483647, 0], [6, 0], [328, 2], [16, 0], [
#         1024, 0], [11, 1], [19, 2], [42, 1],
#     [1162, 3], [51712, 2], [561892, 3], [
#         66561, 9], [6291457, 20], [74901729, 4],
#     [805306373, 25], [1376796946, 5], [1073741825, 29], [1610612737, 28]
# )

# nose
# @parameterized([
#     (9, 2), (529, 4), (20, 1), (1041, 5), (
#         15, 0), (32, 0), (1, 0), (5, 1),
#     (2147483647, 0), (6, 0), (328, 2), (16, 0), (
#         1024, 0), (11, 1), (19, 2), (42, 1),
#     (1162, 3), (51712, 2), (561892, 3), (
#         66561, 9), (6291457, 20), (74901729, 4),
#     (805306373, 25), (1376796946, 5), (
#         1073741825, 29), (1610612737, 28)
# ])

@pytest.mark.parametrize(
    "input_number,expected_result",
    [
        (9, 2), (529, 4), (20, 1), (1041, 5), (
            15, 0), (32, 0), (1, 0), (5, 1),
        (2147483647, 0), (6, 0), (328, 2), (16, 0), (
            1024, 0), (11, 1), (19, 2), (42, 1),
        (1162, 3), (51712, 2), (561892, 3), (
            66561, 9), (6291457, 20), (74901729, 4),
        (805306373, 25), (1376796946, 5), (
            1073741825, 29), (1610612737, 28),
    ],
)
def test_solution_binary_gap(input_number: int, expected_result: int):
    # TODO: make it really working
    # self.assertEqual(expected_result, 1)
    # assert_equal(expected_result, solution(input_number))
    assert expected_result == solution(input_number)


# if __name__ == '__main__':
#     unittest.main()
