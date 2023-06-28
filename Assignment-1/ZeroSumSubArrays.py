#Hash the Running Computation
def zeroSumSubArrays(arr):
    count = 0
    prefix_sum = 0
    sum_count = {0: 1}
    
    for num in arr:
        prefix_sum += num
        if prefix_sum in sum_count:
            count += sum_count[prefix_sum]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
    
print(zeroSumSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7])) #Output: 2
print(zeroSumSubArrays([1, 8, 7, 3, 11, 9])) #Output: 0
print(zeroSumSubArrays([8, -5, 0, -2, 3, -4])) #Output: 2
