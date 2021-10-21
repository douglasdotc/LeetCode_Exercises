# Write a function that return an array containing 
# the shortest combination of numbers that add up to exactly the targetSum

import copy
def bestSum(targetSum:int, nums:list[int]) -> list[int]:
    len_bestSumT = targetSum + 1
    bestSumT = [None]*len_bestSumT
    bestSumT[0] = []

    for t_idx in range(len_bestSumT):
        if bestSumT[t_idx] != None:
            for n in nums:
                if t_idx + n < len_bestSumT:
                    curr_com = copy.copy(bestSumT[t_idx])
                    curr_com.append(n)
                    if bestSumT[t_idx + n] == None or len(curr_com) < len(bestSumT[t_idx + n]):
                        bestSumT[t_idx + n] = curr_com
    
    return bestSumT[targetSum]

print(bestSum(7, [5,3,4,7]))
print(bestSum(7, [2,3]))
print(bestSum(7, [2,4]))
print(bestSum(8, [2,3,5]))
print(bestSum(300, [7, 14]))
print(bestSum(100, [25,1,5,2]))

# Time Complexity:
# Let m = targetSum
# n = length of nums
# double for loop: O(mn)
# copying curr_com: O(m) at most m entries, all 1s
# Overall O(nm^2)

# Space Complexity:
# bestSumT: O(m)
# curr_com: O(m)
# Overall: O(m^2)