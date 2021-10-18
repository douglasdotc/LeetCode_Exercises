# Problem link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# Tags: Google, Apple
"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Example 4:
Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 

Example 5:
Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 

Constraints:

1 <= cardPoints.length <= 105
1 <= cardPoints[i] <= 104
1 <= k <= cardPoints.length
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Maximize the score from start + end of array
        # means minimize the score from a subarray in the middle
        # Sum of a sliding window of integers:
        len_cardPoints = len(cardPoints)
        if k == len_cardPoints:
            return sum(cardPoints)

        sum_k   = sum(cardPoints[-k:])
        max_sum = sum_k # Initialize
        for idx in range(k):
            sum_k  += cardPoints[idx] - cardPoints[len_cardPoints - k + idx]
            max_sum = max(max_sum, sum_k)
        
        return max_sum

# Time complexity:
# Accessing values in array require constant time
# looping over k times --> O(k)

# Space complexity:
# Extra space for sum_k and max_sum is independent of the input array size --> O(1)