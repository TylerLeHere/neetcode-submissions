# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Brute force is that you have like hash set, and remember every node that you visit
        
        #Create the empty hashset
        seen = set()
        current = head
        while current:
            if current in seen:
                return True
            else:
                seen.add(current)
            current = current.next
        
        return False
        