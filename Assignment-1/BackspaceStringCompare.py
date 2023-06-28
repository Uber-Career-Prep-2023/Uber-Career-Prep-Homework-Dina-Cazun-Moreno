#Simultaneous Iteration - Two Pointer

def backspaceStringCompare(s: str, t: str) -> bool:
    def build_string(string: str) -> str:
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)
    
    return build_string(s) == build_string(t)
    
print(backspaceStringCompare("abcde", "abcde"))
print(backspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep"))
print(backspaceStringCompare("abcdef###xyz", "abcw#xyz"))
print(backspaceStringCompare("abcdef###xyz", "abcdefxyz###"))

#Output
#True
#True
#True
#False
