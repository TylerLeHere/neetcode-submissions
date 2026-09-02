# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Brute force: traverse the list, dump all the node pointers into na array, then use two pointer, one from the start 
        # and one at the end, and relink the nodes in order?, then set the last node to be null
        # This one is going to be O(n) time and O(n) space. 
        
        # How to get O(1) space
        # Combinatioin fo three classic linked list techniques
        
        #First step, find the middle of the linked list?
        slow, fast = head, head
        while fast.next and fast.next.next:
            #Shift each pointer
            slow = slow.next
            fast = fast.next.next
        
        #Now split into two halves
        secondListNode = slow.next

        #Terminate the first half
        slow.next = None
        firstListNode = head

        print(f"Before Reverse:")
        self.printList(secondListNode)
        #Second step, reverse the second half?
        secondListNode = self.reverse(secondListNode)
        print(f"After Reverse:")
        self.printList(secondListNode)

        #Third step, Merge the two half by alternating node
        self.merge(firstListNode, secondListNode)
    
    def reverse(self, head: ListNode) -> ListNode:
        # [1] -> [2] -> [3]
        prev = None
        while head:
            #Store next node
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev

    def printList(self, head) -> None:
        while head:
            print(head.val, end = " ")
            head = head.next
        print()

    def merge(self, L1, L2 ) -> None:
        while L1 and L2:
            #Save the next Node of each
            l1_next = L1.next
            l2_next = L2.next
            #Point
            L1.next = L2
            L2.next = l1_next

            L1 = l1_next
            L2 = l2_next



