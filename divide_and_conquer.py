# This pattern involves dividing a data set into smaller chunks and then repeating a process with a subset of data.

# This pattern can tremendously decrease time complexity

# Q1) Given a sorted array of integers, write a function called search, that accepts a value and returns the index where the value passed to the function is located. If the value is not found, return -1

# my solution(=Linear Search): (Time complexity: O(n))

def search(arr=list, n=int):
    if len(arr) < n:
        return -1
    for i in range(0,len(arr)):
        if arr[i] == n:
            return i


# Divide and Conquer Pattern(=Binary Search): (Time complexity: Log(n))

def search(arr=list, n=int):
    min = 0
    max = len(arr) - 1
    while min <= max:
        middle = int((min + max) / 2)
        if arr[middle] < n:
            min = middle + 1
        elif arr[middle] > n:
            max = middle - 1
        else:
            return middle
    return -1



print(search([1,2,3,4,5,6],6))
print(search([1,2,3,4,5,6],4))
print(search([1,2,3,4,5,6],11))