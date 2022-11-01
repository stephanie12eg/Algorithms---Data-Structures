# solution 1
def solution(X, Y, D):
    # write your code in Python 3.8.10
    pass
    jumps = (Y-X)/D

    if int(jumps) < float(jumps):
        return int(jumps)+1 

    return int(jumps)

# solution 2
import math
def solution(X, Y, D):
    # write your code in Python 3.8.10
    pass
    jumps = (Y-X)/D

    return math.ceil(jumps)