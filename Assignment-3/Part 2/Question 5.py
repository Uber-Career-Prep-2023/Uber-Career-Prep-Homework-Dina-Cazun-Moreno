def firstKBinaryNumbers(k):
    res = []
    for i in range(0, k):
        res.append(bin(i).replace("0b", ""))
    return res
