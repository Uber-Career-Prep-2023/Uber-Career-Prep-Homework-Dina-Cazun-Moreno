#Growing/Shrinking Sliding Window
def shortestSubstring(s, required):
    required_chars = set(required)
    left = 0
    right = len(s) - 1
    shortest_length = float('inf')
    while left <= right:
        if set(s[left:right+1]) == required_chars:
            shortest_length = min(shortest_length, right - left + 1)
            left += 1
        else:
            right += 1
    return shortest_length
    
print(shortestSubstring("abracadabra", "abc")) #Ouput: 4
print(shortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx")) #Ouput: 10
print(shortestSubstring("dog", "god")) #Ouput: 3
