# Problem link: https://leetcode.com/problems/binary-search/
# # Practice only

"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

 

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

class Solution:
    def __init__(self) -> None:
        self.nums       = []
        self.len_nums   = 0
        self.target     = 0

    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.len_nums = len(nums)
        self.target = target

        left = 0
        right = self.len_nums - 1
        while left < right:
            mid = (left + right)//2
            if self.nums[mid] < target:
                left = mid + 1
            elif self.nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        if self.nums[left] != target:
            return -1
        return left