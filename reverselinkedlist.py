# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
            
        # Recurse down to the end of the list to find the new head
        new_head = self.reverseList(head.next)
        
        # Reverse the link between head and head.next
        # If 1 -> 2, then head.next.next = head makes 2 -> 1
        head.next.next = head
        head.next = None  # Prevent cycles
        
        return new_head