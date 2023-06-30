#Hash the elements

def missingInteger(n, arr):
    total_sum = (n * (n + 1)) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

n = int(input("Enter the value of n: "))
arr = list(map(int, input("Enter the sorted array: ").split()))

missing_integer = missingInteger(n, arr)
print("Missing integer:", missing_integer)

missingInteger(7, [1, 2, 3, 4, 6, 7]) #Output: 5
missingInteger(2, [1]) #Output: 2
missingInteger(7, [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]) #Output: 9
