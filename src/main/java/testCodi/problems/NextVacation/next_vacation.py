from typing import List


def next_vacation(input_data: List[int]) -> int:
    mapping = ()
    for index in range(len(input_data)):
        mapping.append([input_data[index], (index)])
    return 0
