import pytest
from typing import List
from src.main.java.testCodi.a04PermCheck.perm_check import solution


test_data = [
    ([4, 1, 3, 2], 1),
    ([4, 1, 3], 0)
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_perm_check(input: List[int], expected_result: int):
    assert expected_result == solution(input)
