# Problem link: https://leetcode.com/problems/divide-chocolate/
# Tags: Google

"""
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.
You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, 
each piece consists of some consecutive chunks.
Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.
Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Example 1:
Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

Example 2:
Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.

Example 3:
Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]


Constraints:
0 <= k < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5
"""

# Idea:
# This appears to be a problem to find a way that can give a
# maxi-minimum sweetness --> an optimization problem
# Brute force formulating such an optimization problem will be rather tedious
# Since we would like to find the MAXIMUM minimum magnitude of sweetness that can 
# be attained, we can investigate what will happen along the trend of this value

# Definition: Valid: With the subject getting this level of sweetness,
# the chocolate can still be distributed to all people.

# Observe that the magnitude of sweetness will only be valid until some value.
# If a sweetness s is not valid, any magnitude > s will not valid.
# This is because a larger magnitude of s require more blocks of chocolate
# So we in turns get fewer chunks of chocolates for the people
# To conclude, there will not be a valid value of magnitude s once
# an invalid value is found

class Solution:
    def __init__(self) -> None:
        self.num_people = 0
        self.sweetness  = []

    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # k cuts for k + 1 people:
        self.num_people = k + 1
        self.sweetness  = sweetness

        # Use Binary search tree for the maxi-minimum sweetness:
        # Search boundaries:
        # sweetness cannot less than the minimum sweetness
        left  = min(self.sweetness)
        # Maximum sweetness the subject can get is just the mean()
        # any sweetness > mean() is not possible 
        # since we are distributing the sweetness to n people
        right = sum(self.sweetness)//self.num_people # Integer division

        # Main loop for the tree:
        while left < right: # Terminate when left == right
            guess = (left + right + 1)//2 # Greedy: guess from mid point
            # Note: the mid point should not define as (left + right)//2
            # Consider the case:
            # [valid, valid, valid, invalid, invalid, invalid]
            #                   ^       ^
            #                 left    right
            # With line 80 - 83, using (left + right)//2 will result in an infinity loop

            if self.condition(guess): # Valid
                left  = guess # discard the domain from the original left to guess - 1
            else: # Not valid
                right = guess - 1 # discard the domain form the original guess to right

        assert(left == right)
        return left

    def condition(self, guess:int) -> bool:
        curr_sweetness      = 0
        people_w_chocolate  = 0

        # Distribute chunks of chocolate to each person
        for s in self.sweetness:
            curr_sweetness += s
            # If the cummulative sweetness of the chunk >= guess, break the chocolate
            if curr_sweetness >= guess:
                people_w_chocolate += 1
                curr_sweetness      = 0 # Reset, investigate next chunk
        
        return people_w_chocolate >= self.num_people

# Time Complexity:
# Binary search tree discard half of the values every loop --> O(log(n))
# condition check: for the worst case we need to run through all the entries
# in the array --> O(n)
# Overall time complexity of O(nlog(n))

# Space Complexity:
# Size of additional data stored is independent from the input --> O(1)