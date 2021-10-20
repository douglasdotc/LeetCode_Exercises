# Wtie a function that return an array contaion any combination of numbers >= 0 
# that add up to exactly the targetSum. 
# If there is no combination that adds up to the targetSum, then return null.
# If there are multiple combinations possible, return any single one.

def howSum(nums:list[int], targetSum:int, mem = {}):
    if targetSum in mem:
        return mem[targetSum]

    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    for n in nums:
        remains = targetSum - n
        com = howSum(nums, remains, mem)
        if com != None:
            com.append(n)
            mem[targetSum] = com
            return mem[targetSum]
    
    mem[targetSum] = None
    return mem[targetSum]

print(howSum([2,3], 7))
# print(howSum([5,3,4,7], 7))
# print(howSum([2,4], 7))
# print(howSum([3,5,2], 8))
# print(howSum([7, 14], 300))

# Time complexity:
# O(nm^2), m = targetSum, n = size of array
# mn from the size of the tree
# the extra m from inserting a number at the end of the array com

# Space complexity:
# O(m^2), m = targetSum
# the size of com at most 1xm, there are at most m arrays in the hashmap mem