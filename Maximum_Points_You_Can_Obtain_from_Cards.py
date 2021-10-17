# Problem link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# Tags: Google, Apple

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