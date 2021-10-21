# Write a function that return an array containing 
# the shortest combination of numbers that add up to exactly the targetSum

import copy
def bestSum(nums:list[int], targetSum:int, mem = {}):
    if targetSum in mem:
        return copy.deepcopy(mem[targetSum])

    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortest_com = None
    for n in nums:
        remains = targetSum - n
        com     = bestSum(nums, remains, mem)
        if com != None:
            com.append(n)
            if shortest_com == None or len(com) < len(shortest_com):
                shortest_com = com
    
    mem[targetSum] = shortest_com
    return copy.deepcopy(mem[targetSum])

print(bestSum([2,3], 7, {}))
print(bestSum([2,3,5], 8, {}))
print(bestSum([1,4,5], 8, {}))
print(bestSum([1,2,5,25], 100, {}))

# Expected Expotential complexity O(n^m) for both time ans space