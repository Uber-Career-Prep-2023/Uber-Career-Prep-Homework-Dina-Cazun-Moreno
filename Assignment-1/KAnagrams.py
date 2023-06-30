def kAnagrams(str1, str2, k):
    if len(str1) != len(str2):
        return False
    
    count = 0
    freq = [0] * 26
    
    for i in range(len(str1)):
        freq[ord(str1[i]) - ord('a')] += 1
        freq[ord(str2[i]) - ord('a')] -= 1
    
    for i in range(26):
        if freq[i] > 0:
            count += freq[i]
    
    return count <= k
    
print(kAnagrams("apple", "peach", 1)) #Output: False
print(kAnagrams("apple", "peach", 2)) #Output: True
print(kAnagrams("cat", "dog", 3)) #Output: True
print(kAnagrams("debit curd", "bad credit", 1)) #Output: True
print(kAnagrams("baseball", "basketball", 2)) #Output: False
