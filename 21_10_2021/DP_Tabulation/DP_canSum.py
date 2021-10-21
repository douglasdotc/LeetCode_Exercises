# Given an array of integers, 
# check if there exist a set of integers that can sum to a requested value
# e.g. arr = [1,2,3,4,7], targetSum = 7 --> True
# arr = [1,2,3,4,7], targetSum = 13 --> False

def canSum(targetSum:int, nums:list[int]) -> bool:
    len_canSumT = targetSum + 1
    canSumT = [False]*len_canSumT
    # If targetSum = 0, the result will be true because we no not need to
    # get anything from the array nums
    canSumT[0] = True
    for t_idx in range(len_canSumT):
        if canSumT[t_idx]:
            for n in nums:
                if t_idx + n < len_canSumT:
                    canSumT[t_idx + n] = canSumT[t_idx]
    
    return canSumT[targetSum]

print(canSum(7, [5,3,4,7]))
print(canSum(7, [2,3]))
print(canSum(7, [2,4]))
print(canSum(8, [2,3,5]))
print(canSum(300, [7, 14]))
# Time Complexity
# Let m = targetSum
# n = length of nums
# iterate through 0 to m, for every number iterate through every element of nums --> O(mn)

# Space Complexity
# O(m), just one array of numbers storing booleans