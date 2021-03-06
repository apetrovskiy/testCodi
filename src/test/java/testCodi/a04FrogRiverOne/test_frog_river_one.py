from src.main.java.testCodi.a04FrogRiverOne.solution_frog_river_one \
    import solution
from typing import List
import pytest


test_data = [
    (5, [1, 3, 1, 4, 2, 3, 5, 4], 6),
    (3, [2, 1, 3], 2)
]


# @pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize("number,input_array,expected_result", test_data)
def test_frog_river_one(number: int, input_array: List[int],
                        expected_result: int):
    assert expected_result == solution(number, input_array)
