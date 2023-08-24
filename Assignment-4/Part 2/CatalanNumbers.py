def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def catalanNumber(n):
    catalanNumbers = []
    for i in range(n + 1):
        catalan = factorial(2 * i) // (factorial(i + 1) * factorial(i))
        catalanNumbers.append(catalan)
    return catalanNumbers
