from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional["TreeNode"]) -> int:
        # Step 1: Handle the base case (empty node)
        if not root:
            return 0
        
        # Step 2: Recursively find the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Step 3: Return the greater depth plus 1 for the current root node
        return 1 + max(left_depth, right_depth)