from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack: list[TreeNode] = []
        curr: Optional[TreeNode] = root
        
        while curr or stack:
            # 1. Travel to the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Process the node (Root)
            curr = stack.pop()
            k -= 1
            
            # 3. Check if it's the kth smallest element
            if k == 0:
                return curr.val
            
            # 4. Move to the right subtree
            curr = curr.right
            
        return -1 # Fallback return (guaranteed to not hit per constraints 1 <= k <= n)