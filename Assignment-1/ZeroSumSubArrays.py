#Hash the Running Computation
def zeroSumSubArray(arr):
    
    #create hash map so dictionary
    #then store if sum is in it
    #have a count to see how many subarrays we got
    
    dict = {}
    
    totalSum = 0
    count = 0
    
    for i in range(len(arr)):
        totalSum += arr[i]
        
        if totalSum in dict:
            count += 1
            
        dict[i].append(totalSum)
            
    return count
    
print(zeroSumSubArray([4, 5, 2, -1, -3, -3, 4, 6, -7]))
