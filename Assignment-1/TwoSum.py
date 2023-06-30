#Sliding Window and Hashing Elements
def twoSum(nums, k):
    count = 0
    num_dict = {}
    
    for num in nums:
        complement = k - num
        if complement in num_dict:
            count += num_dict[complement]
        num_dict[num] = num_dict.get(num, 0) + 1
    
    return count
    
print(twoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10)) #Output: 3
print(twoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 9)) #Output: 4
print(twoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6)) #Output: 5
print(twoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1)) #Output: 0
