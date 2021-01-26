from src.main.java.testCodi.a04MaxCounters.max_counters import solution
from typing import List
import pytest


test_data = [
    ()
]


@pytest.mark.parametrize("number,input_array,expected_result", test_data)
def test_max_counters(number: int, input_array: List[int], expected_result: List[int]):
    assert expected_result == solution(number, input_array)
