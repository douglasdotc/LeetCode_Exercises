# Problem link: https://leetcode.com/problems/path-sum-iii/
# Tags: Facebook, Microsoft

"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val    = val
        self.left   = left
        self.right  = right
        
class Solution:
    def __init__(self) -> None:
        self.count      = 0
        self.target_sum = 0
        self.hash_map   = defaultdict(int)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target_sum = targetSum
        self.preorder_traversal(root, 0)
        return self.count

    def preorder_traversal(self, node: TreeNode, curr_sum) -> None:
        if not node:
            return

        # Current prefix sum:
        curr_sum += node.val

        # 2 cases:
        if curr_sum == self.target_sum: # First case: sum from root
            self.count += 1

        # Second case: sub tree
        # += self.hash_map[curr_sum - self.target_sum]
        # is as a result of handling the case where negative values appears
        # e.g. target value = 7
        # a branch of the tree is [2,3,1,-1,1,6]
        # When curr_sum = 12, curr_sum - target_val = 5
        self.count += self.hash_map[curr_sum - self.target_sum]
        
        # Record to hash map
        self.hash_map[curr_sum] += 1

        # DFS search:
        self.preorder_traversal(node.left, curr_sum)
        self.preorder_traversal(node.right, curr_sum)

        # Goiing to visit sibiling node: remove current sum to preserve hash map
        self.hash_map[curr_sum] -= 1

# Time complexity: 
# Need to visit every node. 
# Time complexity is therefore O(n), where n is the number of nodes

# Space complexity:
# Worst case of serching in a hash table is when all elements line up like a linked list
# Therefore the space complexity is of O(n) order