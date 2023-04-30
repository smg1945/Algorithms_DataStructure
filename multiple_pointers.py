# Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition
# Very efficient for solving problems with minimal space complexity as well


# Q1) Write a function called sumZero which accepts a sorted array of integers. The function whould find the first pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if a pair does not exist

# my solution: (Time complexity: O(n^2))

def sumZero(arr=list):
    arr.sort()
    for i in arr:
        diff = i * 2
        if i - diff in arr and i != 0:
            return print([i, i - diff])
    return print('undefined')


# Multiple Pointers Pattern: (Time complexity: O(n), (Space complexity: O(1)))

def countUniqueValues(arr=list):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == 0:
            return [arr[left], arr[right]]
        elif sum > 0:
            right -= 1
        else:
            left += 1
    return print('undefined')



sumZero([-3,-2,-1,0,1,2,3])
sumZero([-2,0,1,3])
sumZero([1,2,3])



# Application of Multiple Pointers Pattern
# Q2) Implement a function called countUniqueValues, which accepts a sorted array, and counts the unique values in the array. There can be negative numbers in the array, but it will always be sorted.


def countUniqueValues(arr=list):
    if len(arr) == 0:
        return 0
    i = 0
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
            j += 1
    return i + 1



countUniqueValues([1,1,1,1,1,2])
countUniqueValues([1,2,3,4,4,4,7,7,12,12,13])
countUniqueValues([])
countUniqueValues([-2,-1,-1,0,1])