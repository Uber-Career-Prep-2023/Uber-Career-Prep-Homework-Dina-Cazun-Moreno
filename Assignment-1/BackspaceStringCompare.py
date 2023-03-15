#Simultaneous Iteration - Two Pointer

def backspaceStringCompare(s1, s2):
    
    #save s1 and s2 into list array bc strings are immutable
    
    stringOne = list(s1).reverse()
    stringTwo = list(s2).reverse()
    
    if stringOne == stringTwo:
        return True
    else:
        for i in range(len(stringOne)):
            for j in range(len(stringTwo)):
                if stringTwo[j] == "#":
                    del stringTwo[j]
                    del stringTwo[j+1]
                if stringOne == stringTwo:
                    return True
                else:
                    return False
    
print(backspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep"))
print(backspaceStringCompare("poop", "poop"))
print(backspaceStringCompare("abcdef###xyz", "abcw#xyz"))
print(backspaceStringCompare("abcdef###xyz", "abcdefxyz###"))
