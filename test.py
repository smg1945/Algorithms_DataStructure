def minSubArrayLen(arr, num):
    if not arr:  # If the array is empty, return 0
        return 0
    
    left = 0  # Starting index of the subarray
    right = 0  # Ending index of the subarray
    total = 0  # Sum of the current subarray
    min_len = float('inf')  # Initialize the minimum length to infinity
    
    while left < len(arr):
        if total < num and right < len(arr):
            total += arr[right]
            right += 1
        elif total >= num:
            min_len = min(min_len, right - left)
            total -= arr[left]
            left += 1
        else:
            break
    
    if min_len == float('inf'):  # If there isn't a subarray with the sum >= num, return 0
        return 0
    else:
        return min_len
    


print(minSubArrayLen([2,3,1,2,4,3], 7))
print(minSubArrayLen([2,1,6,5,4], 9))
print(minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52))
print(minSubArrayLen([1,4,16,22,5,7,8,9,10],39))
print(minSubArrayLen([1,4,16,22,5,7,8,9,10],55))
print(minSubArrayLen([4, 3, 3, 8, 1, 2, 3], 11))
print(minSubArrayLen([1,4,16,22,5,7,8,9,10],95))