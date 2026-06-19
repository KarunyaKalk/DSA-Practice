from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result: List[List[int]] = []
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_nodes = deque()  # Using a deque for O(1) left/right insertions

            for _ in range(level_size):
                curr = queue.popleft()

                # Insert value based on current direction
                if left_to_right:
                    level_nodes.append(curr.val)
                else:
                    level_nodes.appendleft(curr.val)

                # Add child nodes normally (left to right) to the main queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # Add the current finished level to our final result
            result.append(list(level_nodes))

            # Flip the direction flag for the next level
            left_to_right = not left_to_right

        return result