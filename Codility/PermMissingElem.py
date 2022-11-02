# solution 1
def solution(A):
    # write your code in Python 3.8.10
    pass
    if len(A)==0:
        return 1
    A.sort()
    if A[0] != 1:
        return 1
    for i in range(len(A)-1):
        if A[i]+1 != A[i+1]:
            return A[i]+1 
    return A[-1]+1

# solution 2
def solution(A):
    # write your code in Python 3.8.10
    pass
    if len(A)==0:
        return 1
    A.sort()
    for i in range(len(A)-1):
        if A[i] != i+1:
            return i+1 
    return A[-1]+1

# solution 3
def solution(A):
    expected_sum = ((len(A) + 1) * (len(A) + 2)) // 2
    return expected_sum - sum(A)

# solution 4
def solution(A):
    array = [0] * (len(A) + 1) # The array value will still be 0 and not change if the number is not present in A
    for number in A:
        array[number - 1] = number
    for i in range(len(array)):
        if array[i] == 0:
            return i + 1