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
    
print(dedupArray([1, 3, 4, 8, 10, 12]))

#Output
#[1, 3, 4, 8, 10, 12]
