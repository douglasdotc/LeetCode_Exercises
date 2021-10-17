# Problem Link: https://leetcode.com/problems/validate-stack-sequences/
# Tags: Google, Facebook, Adobe, Zoho

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack   = [] # Initialize empty stack
        po_idx  = 0
        for pu_idx in range(len(pushed)):
            stack.append(pushed[pu_idx])
            # pop until it is empty or unexpected popping sequence is found
            while stack and stack[-1] == popped[po_idx]:
                stack.pop()
                po_idx += 1

        return po_idx == len(popped)

# Time Complexity:
# Visiting pushed[], appending to stack[], popping require constant time
# Using for loop for pushed[] and while loop for popped[] --> O(n), n = len(pushed) + len(popped)
# because they visited different array even though they are organized in a nested way

# Space Complexity:
# The array stack requires O(n)