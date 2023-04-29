#Hash the elements

def missingInteger(arr, n):
    
    #create hashmap of all nums 1 - n. set frequency or count of each element to 0.
    #key will num. value will frequency
    #go through array and have counter or frequency increment if num in array is in hashmap
    #if any key's value in hashmap is 0 then return that key
    hashmap = {}
    
    for i in range(1, n+1):
        hashmap[i] = 0
        
    for i in range(len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]] += 1
    
    for key in hashmap:
        if hashmap[key] == 0:
            return key
        
print(missingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12))

#Output
#9
