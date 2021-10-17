# Problem link: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# Tags: Google

class Solution:
    def __init__(self) -> None:
        self.rotations_top      = 0
        self.rotations_bottom   = 0
        self.num_dominos        = 0
        self.tops               = []
        self.bottoms            = []

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        self.num_dominos = len(tops)
        self.tops        = tops
        self.bottoms     = bottoms

        self.rotations_top = self.check(self.tops[0])
        if self.rotations_top == -1 and self.tops[0] != self.bottoms[0]:
            self.rotations_bottom = self.check(self.bottoms[0])
            return self.rotations_bottom
        
        return self.rotations_top

    def check(self, d_0:int) -> int:
        rotation_up     = 0
        rotation_down   = 0
        for idx in range(self.num_dominos):
            # Check if ith domino is a complete stranger to other dominos
            if self.tops[idx] != d_0 and self.bottoms[idx] != d_0:
                return -1
            
            # If the top number != d_0, the bottom one must = d_0, 
            # flip with respect to top side
            elif self.tops[idx] != d_0:
                rotation_up += 1

            # If the bottom number != d_0, the top one must = d_0, 
            # flip with respect to bottom side
            elif self.bottoms[idx] != d_0:
                rotation_down += 1

        return min(rotation_up, rotation_down)

# Time complexity: 1 for loop looking at all the values in tops and bottoms --> O(n)
# Space complexity: returning just a number: 
# Either self.rotations_top or self.rotations_bottom, 
# this is independent of the input array size. --> O(1)