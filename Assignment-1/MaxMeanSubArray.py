#Sliding window

#mean = average of numbers. since k is fixes, max sum gives us the highest mean sum

def maxMeanSubArray(arr, k):
    n = len(arr)
    if k > n:
        return None
    
    max_mean = 0
    curr_sum = sum(arr[:k])
    
    for i in range(n - k + 1):
        curr_mean = curr_sum / k
        max_mean = max(max_mean, curr_mean)
        
        if i + k < n:
            curr_sum = curr_sum - arr[i] + arr[i + k]
    
    return max_mean
    
print(maxMeanSubArray([4, 5, -3, 2, 6, 1], 2)) #Output: 4.5
print(maxMeanSubArray([4, 5, -3, 2, 6, 1], 3)) #Output: 3.0
print(maxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3)) #Output: 1.0
print(maxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5)) #Output: 1.0
