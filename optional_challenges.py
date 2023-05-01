# Q1) write a function called sameFrequency. Given two positive integers, find out if the two numbders have the same frequency of digits. (condition: Time complexity = O(n))

def sameFrequency(a=int, b=int):
    num1 = str(a)
    num2 = str(b)
    assert a and b > 0, "arguments must be positives, but given is negative."
    if len(num1) != len(num2):
        return False
    frequencyCounterA = {}
    frequencyCounterB = {}
    for i in num1:
        frequencyCounterA[i] = frequencyCounterA.get(i, 0) + 1
    for i in num2:
        frequencyCounterB[i] = frequencyCounterB.get(i, 0) + 1
    for key in frequencyCounterA:
        if key not in frequencyCounterB:
            return False
        elif frequencyCounterA[key] != frequencyCounterB[key]:
            return False
    return True


print(sameFrequency(182, 281))
print(sameFrequency(34, 14))
print(sameFrequency(3589578, 5879385))
print(sameFrequency(22, 222))



# Q2) Implement a function called, areThereDuplicates which accepts a variable number of arguments, and checks whether there are any duplicates among the arguments passed in. (condition: Time complexity = O(n), Space complexity = O(n). You can solve this using the frequency counter pattern OR the multiple pointers pattern)

def areThereDuplicates(*args):
    frequencyCounter = {}
    for val in args:
        frequencyCounter[val] = frequencyCounter.get(val, 0) + 1
        if frequencyCounter[val] > 1:
            return True
    return False



print(areThereDuplicates(1, 2, 3))
print(areThereDuplicates(1, 2, 2))
print(areThereDuplicates('a', 'b', 'c', 'a'))



# Q3) Write a function called averagePair. Given a sorted array of integers and a target average, determine if there is a pair of values in the array where the average of the pair equals the target average. There may be more than one pair that matches the average target.

def averagePair(arr=list, target=float):
    start = 0
    end = len(arr) - 1
    while start < end:
        avg = (arr[start]+arr[end]) / 2
        if avg == target:
            return True
        elif avg < target:
            start += 1
        else:
            end -= 1
    return False



averagePair([1,2,3],2.5)
averagePair([1,3,3,5,6,7,10,12,19],8)
averagePair([-1,0,3,4,5,6],4.1)
averagePair([],4)



# Q4) Write a function called isSubsequence which takes in two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. In other words, the function should check whether the characters in the first string appear somewhere in the second string, without their order changing. (Your solution MUST have AT LEAST the following complexities: Time Complexity - O(N + M), Space Complexity - O(1))

def isSubsequence(str1=str, str2=str):
    i = 0
    j = 0
    if not str1:
        return True
    while j < len(str2):
        if str2[j] == str1[i]:
            i += 1
        if i == len(str1):
            return True
        j += 1
    return False



isSubsequence('hello', 'hello world')
isSubsequence('sing', 'sting')
isSubsequence('abc', 'abracadabra')
isSubsequence('abc', 'acb')



# Q5) Given an array of integers and a number, write a function called maxSubarraySum, which finds the maximum sum of a subarray with the length of the number passed to the function. Note that a subarray must consist of consecutive elements from the original array. 

def maxSubarraySum(arr=list, n=int):
    if len(arr) < n:
        return 'null'
    total = 0
    for i in range(0, n):
        total += arr[i]
    currentTotal = total
    for i in range(n, len(arr)):
        currentTotal += arr[i] - arr[i-n]
        total = max(total, currentTotal)
    return total



maxSubarraySum([100,200,300,400], 2)
maxSubarraySum([1,4,2,10,23,3,1,0,20], 4)
maxSubarraySum([-3,4,0,-2,6,-1], 2)
maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2)
maxSubarraySum([2,3], 3)



# Q6) Write a function called minSubArrayLen which accepts two parameters - an array of positive integers and a positive integer. This function should return the minimal length of a contiguous subarray of which the sum is greater than or equal to the integer passed to the function. If there isn't one, return 0 instead.

def minSubArrayLen(arr=list, num=int):
    total = 0
    start = 0
    end = 0
    minLen = float('inf')
    while start < len(arr):
        if total < num and end < len(arr):
            total += arr[end]
            end += 1
        elif total >= num:
            minLen = min(minLen, end-start)
            total -= arr[start]
            start += 1
        else:
            break
    if minLen == float('inf'):
        return 0
    else:
        return minLen



minSubArrayLen([2,3,1,2,4,3], 7)
minSubArrayLen([2,1,6,5,4], 9)
minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52)
minSubArrayLen([1,4,16,22,5,7,8,9,10],39)
minSubArrayLen([1,4,16,22,5,7,8,9,10],55)
minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11)
minSubArrayLen([1,4,16,22,5,7,8,9,10],95)



# Q7) Write a function called findLongestSubstring, which accepts a string and returns the length of the longest substring with all distinct characters.

def findLongestSubstring(str=str):
    longest = 0
    seen = {}
    start = 0
    for i in range(0, len(str)):
        char = str[i]
        if seen[char]:
            start = max(start, seen[char])
        longest = max(longest, i - start + 1)
        seen[char] = i + 1
    return longest



findLongestSubstring('')
findLongestSubstring('rithmschool')
findLongestSubstring('thisisawesome')
findLongestSubstring('thecatinthehat')
findLongestSubstring('bbbbbb')
findLongestSubstring('longestsubstring')
findLongestSubstring('thisishowwedoit')