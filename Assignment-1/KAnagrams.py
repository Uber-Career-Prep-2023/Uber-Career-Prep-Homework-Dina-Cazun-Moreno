def kAnagrams(s1, s2, k):
    
    #create hashmap of the characters of first string. set frequency or count of each char to 1.
    #key will char. value will be frequency.
    #go through second string and have counter or frequency decrement if char in second string is in hashmap
    #if hashmap's values added together are greater than k, then not anagrams.
    
    hashmap = {}
    counterValue = 0
    frequency = 0
    
    for i in range(len(s1)):
        hashmap[s1[i]] = 1 #key and value assignment
        if hashmap[s1[i]] in hashmap:
            hashmap[s1[i]] += 1
    
    print(hashmap)
        
    for i in range(len(s2)):
        if s2[i] in hashmap:
            hashmap[s2[i]] -= 1
            
    print(hashmap)
            
    for value in hashmap.values():
        if value == 1:
            counterValue += 1
            
    if counterValue > k:
        return False
    else:
        return True
        
print(kAnagrams("apple", "peach", 1))

#Output
#{'a': 1, 'p': 1, 'l': 1, 'e': 1}
#{'a': 0, 'p': 0, 'l': 1, 'e': 0}
#True
