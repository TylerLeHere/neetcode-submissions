# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Align on a few constraints
        # The list has at least one node, so head is never None
        # n is always strictly valid: It can not be negative, zero or exceeed the list length?
        #
        # My baseline thought is the two-pass approach. 
        # PassOne: I walk the list to find the total length, let's call it L.
        #Pass two: I walk the list again stopping at node (L - n - 1) to safely bypass the target node. Going to be O(L) time
        


        #Dummy Node
        dummy = ListNode(0, head)

        #Initialize left pointer to dummy
        leftP = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n = n - 1 #When n = 0 that means we shifted the amount that we want to do

        #Now we are goint to shift left and right until right reaches the end of the list
        
        while right:
            leftP = leftP.next
            right = right.next
        
        #delete
        leftP.next = leftP.next.next #Shifted by 1 to delete

        return dummy.next

