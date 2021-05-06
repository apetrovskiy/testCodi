from src.main.java.testCodi.a02OddOccurrencesInArray.solution \
    import solution_odd_occurrences
import pytest
from typing import List


@pytest.mark.parametrize(
    "input_array,expected_result",
    [
        ([9, 3, 9, 3, 9, 7, 9], 7),
        ([2, 2, 3, 3, 4], 4),
        ([42], 42)
    ],
)
def test_odd_occurrences_in_array(input_array: List[int],
                                  expected_result: int):
    assert expected_result == solution_odd_occurrences(input_array)
