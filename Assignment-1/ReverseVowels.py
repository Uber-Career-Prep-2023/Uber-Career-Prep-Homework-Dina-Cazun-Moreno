#Two Pointer
def reverseVowels(s):
    
    vowels = set(list("aeiouAEIOU"))
    
    s = list(s)
    
    i = 0
    j = len(s) - 1
    
    while i < j:
        if(s[i] in vowels and s[j] in vowels):
            s[i] = s[j]
            s[j] = s[i]
          
        i += 1  
        j -= 1
            
    return "".join(s)


print(reverseVowels("flamingo"))
