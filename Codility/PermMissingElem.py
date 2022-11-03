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
        array[number - 1] = number # adds items in array A to 'array' and sorts by specifying index 
    for i in range(len(array)):
        if array[i] == 0: # first 0 encountered is where there is a missing value. The result is the index value +1. This is why array was mutiplied by len(A)+1 to accomodate for the result being A[-1]+1
            return i + 1