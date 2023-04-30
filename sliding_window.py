# This pattern involves creating a window which can either be an array or number from one position to another

# Depending on a certain condition, the window either increases or closes (and a new window is created)

# Very useful for keeping track of a subset of data in an array/string etc.


# Q1) Write a function called maxSubarraySum which accepts an array of integers and a number called n. The function should calculate the maximum sum of n consecutive elements in the array.

# my solution:

def maxSubarraySum(arr=list, n=int):
    if len(arr) < n:
        return 'null'
    result = []
    i = 0
    while i + n <= len(arr):
        s = sum(arr[i:i+n])
        i += 1
        result.append(s)
    return max(result)
        

# Sliding Window Pattern: (Time complexity: O(n))

def maxSubarraySum(arr=list, n=int):
    maxSum = 0
    tempSum = 0
    if len(arr) < n:
        return 'null'
    for i in range(0, n):
        maxSum += arr[i]
    tempSum = maxSum
    for i in range(n, len(arr)):
        tempSum = tempSum - arr[i - n] + arr[i]
        maxSum = max(maxSum, tempSum)
    return maxSum



print(maxSubarraySum([1,2,5,2,8,1,5],2))
print(maxSubarraySum([1,2,5,2,8,1,5],4))
print(maxSubarraySum([4,2,1,6],1))
print(maxSubarraySum([4,2,1,6,2],4))
print(maxSubarraySum([],4))