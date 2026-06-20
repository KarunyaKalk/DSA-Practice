from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        # Initialize a queue with the left and right children of the root
        queue = deque([root.left, root.right])
        
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            
            # If both are None, continue checking the rest of the queue
            if not t1 and not t2:
                continue
            # If one is None or values misalign, it's not symmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False
                
            # Push children in mirrored order
            queue.append(t1.left)
            queue.append(t2.right) # t1.left mirrors t2.right
            
            queue.append(t1.right)
            queue.append(t2.left)  # t1.right mirrors t2.left
            
        return True