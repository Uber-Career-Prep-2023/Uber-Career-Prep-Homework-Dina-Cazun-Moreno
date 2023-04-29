#Sliding Window and Hashing Elements
def twoSum(arr, k):
    
    #sliding window because the window will be 2 since we are looking for pairs
    #find the matching element to the sum with reference to the current num at index
    #if it is in the hashmap, then we output that pair: the num at the index and the matching element
    
    hashmap = {}
    
    for i in range(len(arr)):
        matchingElement = k - arr[i]
        if difference in hashmap:
            print("Pairs: " "(", arr[i], ",", difference,")")
    
print(twoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))

#Output
#Traceback (most recent call last):
  #File "/Users/dinacazun/UCP_HW1.py", line 15, in <module>
    #print(twoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))
  #File "/Users/dinacazun/UCP_HW1.py", line 12, in twoSum
    #if difference in hashmap:
#NameError: name 'difference' is not defined
