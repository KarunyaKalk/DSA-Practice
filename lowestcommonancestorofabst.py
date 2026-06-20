from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr: Optional['TreeNode'] = root
        
        while curr:
            # Case 1: Both p and q are in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Case 2: Both p and q are in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # Case 3: We found the split point (or found p or q itself)
            else:
                return curr
                
        return root  # Fallback return statement