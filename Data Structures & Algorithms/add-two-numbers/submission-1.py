# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Maintain two pointers, one for each list, and a carry
        # variable initialized to 0

        #While either list still has nodes, I will take the current digit from each list and add them along with carry, create a new node containing sum % 10. Then I will update the carry to sum / 10

        #After both lists are done, if this is still a carry, create a node for it?

        
        ########

        # Create a dummy node
        dummy = ListNode()

        #Current Pointer to Dummy
        currentP = dummy
        carry = 0

        while l1 or l2:
            #Read the current digit of each list (0 if already ended)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #Now we add all the digits with the carry
            currentSum = v1 + v2 + carry

            #Calculate the digit
            digit = currentSum % 10

            #Calculate the carry over
            carry = currentSum // 10

            currentP.next = ListNode(digit)
            currentP = currentP.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            currentP.next = ListNode(carry)
        
        return dummy.next


        