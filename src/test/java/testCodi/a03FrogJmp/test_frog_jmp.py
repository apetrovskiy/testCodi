from target.classes.testCodi.a03FrogJmp.frog_jmp import solution_frog_jmp
import pytest


@pytest.mark.parametrize(
    "x,y,d,expected_result",
    [
        (10, 85, 30, 3),
        (10, 234_342_345, 8, 29_292_792),
        (10, 234_342_345, 1, 234_342_335),
        (10, 2_234_342_345, 1, 2_234_342_335),
        (10, 2_234_342_345, 1_000_000_000, 3),
        (100, 100, 2, 0)
    ],
)
def test_frog_jmp(x: int, y: int, d:int, expected_result: int):
    assert expected_result == solution_frog_jmp(x, y, d)
