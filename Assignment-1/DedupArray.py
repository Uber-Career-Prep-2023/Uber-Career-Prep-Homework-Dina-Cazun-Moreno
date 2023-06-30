#Hash the Elements?
def dedupArray(arr):
    
    #returning a new list, so create new list as empty
    #iterate through given arr and if element is not in the new list, add it to new list
    #if we have seen it (meaning duplicates), then we don't add it
    #return new list
    #iterate through array and put each number into hashmap
    
    newArray = []
    
    for element in arr:
        if element not in newArray:
            newArray.append(element)
    
    return newArray
    
print(dedupArray([1, 3, 4, 8, 10, 12])) #Output: [1, 3, 4, 8, 10, 12]
print(dedupArray([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15])) #Output: [0, 1, 4, 5, 8, 9, 10, 11, 15]
print(dedupArray([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])) #Output: [1, 2, 3, 4]
