from typing import Optional

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional['ListNode'] = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edge Case: An empty list or a single node cannot form a loop
        if not head or not head.next:
            return False
            
        # Initialize both pointers at the starting line (head)
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        
        # Guard condition: Ensure fast and fast.next are valid before jumping
        while fast and fast.next:
            assert slow is not None  # Guaranteed by loop condition
            slow = slow.next          # Moves 1 step at a time
            fast = fast.next.next     # Moves 2 steps at a time
            
            # If they meet, a cycle exists
            if slow == fast:
                return True
                
        # If the loop breaks, the fast pointer reached the end (None) -> No cycle!
        return False