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

#Output
#Traceback (most recent call last):
  #File "/Users/dinacazun/UCP_HW1.py", line 23, in <module>
    #print(zeroSumSubArray([4, 5, 2, -1, -3, -3, 4, 6, -7]))
  #File "/Users/dinacazun/UCP_HW1.py", line 19, in zeroSumSubArray
    #dict[i].append(totalSum)
#KeyError: 0
