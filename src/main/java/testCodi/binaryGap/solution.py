# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary = str(bin(N))
    max_gap = 0
    previous_one = binary.find('1')
    if previous_one == -1:
        return max_gap
    binary = binary[previous_one + 1:]
    while len(binary) > 0:
        current_one = binary.find('1')
        if current_one != -1:
            if max_gap < current_one:
                max_gap = current_one
            binary = binary[current_one + 1:]
            previous_one = current_one
        else:
            break
        
    return max_gap
