def reverseWords(s):
    words = s.split()
    return ' '.join(words[::-1])

print(reverseWords("Uber Career Prep"))
#output: Prep Career Uber
print(reverseWords("Emma lives in Brooklyn, New York."))
#output: York. New Brooklyn, in lives Emma
