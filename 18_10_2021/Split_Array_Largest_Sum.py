# Problem Link: https://leetcode.com/problems/split-array-largest-sum/description/
# Tags: Google, Apple, Amazon

"""
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

 
Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4
 
Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
"""

# Idea:
# Concerning the largest sum of the subarrays L_subarr_sum, there exist a value L_subarr_sum*
# such that all L_subarr_sum >= L_subarr_sum* are valid.
# By valid, we refer to the ability of splliting the given array into m subarrays
# with all the cummulative sum of the subarrays <= L_subarr_sum

class Solution:
    def __init__(self) -> None:
        self.num_subarr_lim = 0
        self.nums           = []

    def splitArray(self, nums: List[int], m: int) -> int:
        self.num_subarr_lim = m
        self.nums           = nums

        # Lower bound is the largest entry in the given array
        # It is not the smallest entry because we are finding the largest sum of subarrays
        # For a case the largest sum is when the largest entry stays alone
        min_L_subarr_sum = max(self.nums)

        # Upper bound is the sum of the whole given array, 
        # because we can return just the entire given array
        max_L_subarr_sum = sum(self.nums)

        # Main Loop:
        while min_L_subarr_sum < max_L_subarr_sum:
            mid_L_subarr_sum = (min_L_subarr_sum + max_L_subarr_sum)//2
            if self.condition(mid_L_subarr_sum): # Valid
                max_L_subarr_sum = mid_L_subarr_sum # Discard value beyond mid_L_subarr_sum
            else: # Not valid
                min_L_subarr_sum = mid_L_subarr_sum + 1 # Discard values <= mid_L_subarr_sum

        return min_L_subarr_sum

    def condition(self, mid_L_subarr_sum:int) -> bool:
        L_subarr_sum = 0
        num_subarr   = 1 # At least there is one array
        for n in self.nums:
            L_subarr_sum += n
            if L_subarr_sum > mid_L_subarr_sum: # Exceed proposing sum
                L_subarr_sum = n # pass the latest number to next array
                num_subarr  += 1 # next array
                if num_subarr > self.num_subarr_lim: # If need more than sub array limits
                    return False

        return True

# Time Complexity:
# Binary search tree discard half of the values every loop --> O(log(n))
# condition check: for the worst case we need to run through all the entries
# in the array --> O(n)
# Overall time complexity of O(nlog(n))

# Space Complexity:
# Size of additional data stored is independent from the input --> O(1)