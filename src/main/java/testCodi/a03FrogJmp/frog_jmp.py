# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution_frog_jmp(X, Y, D):
    # write your code in Python 3.6
    if X == Y:
        return 0
    candidate = int((Y - X) / D)
    if X + candidate * D >= Y:
        return candidate
    else:
        return candidate + 1
