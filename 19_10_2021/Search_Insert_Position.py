# Problem link: https://leetcode.com/problems/search-insert-position/
# Tags: Facebook, Google

"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

class Solution:
    def __init__(self) -> None:
        self.nums       = []
        self.len_nums   = 0
        self.target     = 0

    def searchInsert(self, nums: List[int], target: int) -> int:
        self.nums       = nums
        self.len_nums   = len(self.nums)
        self.target     = target

        left  = 0
        right = self.len_nums - 1
        while left <= right: 
            # L <= R to take care of the case 
            # when the target is not in the list
            mid = (left + right)//2
            if self.nums[mid] < self.target:
                left = mid + 1
            elif self.nums[mid] > self.target:
                right = mid - 1
            else:
                return mid

        return left