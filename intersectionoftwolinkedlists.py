from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Edge case: If either list is empty, there can be no intersection
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB
        
        # Loop continues until pointers meet (either at a node or both at None)
        while pA != pB:
            # Move pA to next node, or redirect to headB if at the end
            pA = pA.next if pA else headB
            
            # Move pB to next node, or redirect to headA if at the end
            pB = pB.next if pB else headA
            
        # Returns either the intersection node or None
        return pA