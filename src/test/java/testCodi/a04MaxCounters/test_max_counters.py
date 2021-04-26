from src.main.java.testCodi.a04MaxCounters.max_counters import solution
from typing import List
import pytest


test_data = [
    (5, [3, 4, 4, 6, 1, 4, 4], [3, 2, 2, 4, 2])
]


# @pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize("number,input_array,expected_result", test_data)
def test_max_counters(number: int,
                      input_array: List[int], expected_result: List[int]):
    assert expected_result == solution(number, input_array)
