# Wtie a function that return an array contaion any combination of numbers >= 0 
# that add up to exactly the targetSum. 
# If there is no combination that adds up to the targetSum, then return null.
# If there are multiple combinations possible, return any single one.

import copy
def howSum(targetSum:int, nums:list[int]) -> list[int]:
    len_howSumT = targetSum + 1
    howSumT = [None]*(len_howSumT)
    howSumT[0] = []

    for t_idx in range(len_howSumT):
        if howSumT[t_idx] != None:
            for n in nums:
                if t_idx + n < len_howSumT:
                    howSumT[t_idx + n] = copy.copy(howSumT[t_idx])
                    howSumT[t_idx + n].append(n)
    
    return howSumT[targetSum]


print(howSum(7, [5,3,4,7]))
print(howSum(7, [2,3]))
print(howSum(7, [2,4]))
print(howSum(8, [2,3,5]))
print(howSum(300, [7, 14]))

# Time Complexity:
# Let m = targetSum
# n = length of nums
# O(mn) for double for loop
# Copying: O(m)
# Overall O(nm^2)

# Space Complexity:
# O(m^2): howSumT: O(m), every entry in the array to be copied at most O(m)
# Overall O(m^2)