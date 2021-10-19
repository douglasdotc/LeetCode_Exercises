# Problem link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
# Tags: Facebook, Google

"""
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
 

Constraints:
1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500
"""

# Idea:
# Concerning weight capacity, there will exist some value C_w* such that
# C_w >= C_w* will always valid. This is because a ship with larger capacity
# can always contain packages with cummulative weight <= C_w

class Solution:
    def __init__(self) -> None:
        self.weights  = []
        self.deadline = 0

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights    = weights
        self.deadline   = days

        left_min_weight  = max(self.weights) # At least can carry the heaviest package in the list
        right_max_weight = sum(self.weights) # At most carry all of them in one shot

        # Main loop:
        while left_min_weight < right_max_weight:
            mid_weight = (left_min_weight + right_max_weight)//2 # Greedy approach
            if self.condition(mid_weight):
                right_max_weight = mid_weight
            else:
                left_min_weight  = mid_weight + 1
                
        return left_min_weight

    def condition(self, mid_weight:int) -> bool:
        # Check whether all packages can be finished shipping in required days:
        days        = 1 # At least one day
        cum_weight  = 0 # Cummulative weight for a shippment

        for w in self.weights:
            cum_weight += w
            if cum_weight > mid_weight:
                cum_weight   = w # Pass the latest package to next day
                days        += 1
                if days > self.deadline: # 
                    return False

        return True # Can ship within deadline

# Time Complexity:
# Binary search tree discard half of the values every loop --> O(log(n))
# condition check: for the worst case we need to run through all the entries
# in the array --> O(n)
# Overall time complexity of O(nlog(n))

# Space Complexity:
# Size of additional data stored is independent from the input --> O(1)