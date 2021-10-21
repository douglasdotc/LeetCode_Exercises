# Given an array of integers, 
# check if there exist a set of integers that can sum to a requested value
# e.g. arr = [1,2,3,4,7], targetSum = 7 --> True
# arr = [1,2,3,4,7], targetSum = 13 --> False

# DP approach:
# targetSum - every entry of the given array
# if there exist a combination that can sum up to targetSum
# the subtraction will eventually reach zero
def canSum(nums:list[int], targetSum:int, mem = {}) -> bool:
    if targetSum in mem:
        return mem[targetSum]

    if targetSum == 0:
        return True
    
    if targetSum < 0:
        return False
    
    for n in nums:
        remains = targetSum - n
        if canSum(nums, remains, mem):
            mem[targetSum] = True
            return mem[targetSum]

    mem[targetSum] = False
    return mem[targetSum]

print(canSum([2,3], 7, {}))
print(canSum([5,3,4,7], 7, {}))
print(canSum([2,4], 7, {}))
print(canSum([7, 14], 300, {}))

# Time complexity
# O(mn) where m = target sum, n = array length
# Stored all the results from subtree and reuse it when encountered again
# at most mn combinations

# Space complexity:
# O(m), at most store True or False for every number < m, m = targetSum