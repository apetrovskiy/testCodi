from src.main.java.testCodi.problems.NextVacation.next_vacation \
    import next_vacation
from typing import List
import pytest


test_data = [
    ([7, 3, 7, 3, 1, 3, 4, 1], 5),
    ([2, 1, 1, 3, 2, 1, 1, 3], 3),
    ([7, 5, 2, 7, 2, 7, 4, 7], 6)
]


@pytest.mark.parametrize("input,expected_result", test_data)
def test_next_vacation(input: List[int], expected_result: int):
    assert expected_result == next_vacation(input)
