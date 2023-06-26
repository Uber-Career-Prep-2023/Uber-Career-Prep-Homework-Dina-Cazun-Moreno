#Question 5: firstKBinaryNumbers

def firstKBinaryNumbers(k):
    res = []
    for i in range(0, k):
        res.append(bin(i).replace("0b", ""))
    return res

print(firstKBinaryNumbers(5))
#output: ['0', '1', '10', '11', '100']

print(firstKBinaryNumbers(10))
['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']
