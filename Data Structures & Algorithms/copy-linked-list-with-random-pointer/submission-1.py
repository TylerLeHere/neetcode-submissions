"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None} #null is going to map to null for one edge case

        #Iterate through the linked list once

        current = head
        while current:
            #Create a copy of that node
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next

        #Now running the loop one more time
        #Setting the current to the beginning of LinkedList
        current = head
        while current:
            #Set the pointer
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next] #One edge case which is current.next is null

            copy.random = oldToCopy[current.random]
            current = current.next
        
        return oldToCopy[head]

        