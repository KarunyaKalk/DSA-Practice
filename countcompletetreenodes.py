from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        left_h = get_height(root.left)
        right_h = get_height(root.right)
        
        # If left and right heights are equal, the left subtree is perfect
        if left_h == right_h:
            # 1 (root) + (2^left_h - 1) (left subtree) + countNodes(right subtree)
            # equivalent to: (1 << left_h) + self.countNodes(root.right)
            return (1 << left_h) + self.countNodes(root.right)
        else:
            # If heights are different, the right subtree is perfect (but one level shorter)
            # 1 (root) + (2^right_h - 1) (right subtree) + countNodes(left subtree)
            # equivalent to: (1 << right_h) + self.countNodes(root.left)
            return (1 << right_h) + self.countNodes(root.left)