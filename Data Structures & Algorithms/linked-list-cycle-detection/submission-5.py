# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Brute force is that you have like hash set, and remember every node that you visit
        
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next

            slow = slow.next
            if fast == slow:
                return True        
        #It does not exist the cycle
        return False
        