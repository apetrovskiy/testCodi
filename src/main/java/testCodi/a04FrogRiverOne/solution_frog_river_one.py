from src.test.java.testCodi.a04FrogRiverOne.test_frog_river_one import solution
from typing import List
import pytest


test_data = [
    (5, [1, 3, 1, 4, 2, 3, 5, 4], 6)
]


@pytest.mark.parametrize("number,input_array,expected_result", test_data)
def test_frog_river_one(number: int, input_array: List[int], expected_result: int):
    assert expected_result == solution(number, input_array)
