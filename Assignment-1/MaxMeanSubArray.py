#Sliding window

#mean = average of numbers. since k is fixes, max sum gives us the highest mean sum

def maxMeanSubArray(arr, k):
    
    if k > len(arr):
        return -1
    
    maxSum = 0
    
    for i in range(len(arr)-k+1):
        currentSum = arr[i] + arr[i+k-1]
        if currentSum > maxSum:
            maxSum = currentSum
            
    return maxSum/k
    
print(maxMeanSubArray([4, 5, -3, 2, 6, 1], 2))
