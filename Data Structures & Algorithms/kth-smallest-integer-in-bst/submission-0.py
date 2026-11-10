# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Iterative solution is not quite as hard

        # N tell us the number of elements we have visited from the tree
        
        # current: the node you are exploring
        # stack: nodes saved so you can come back to them
        # n : how many nodes you have visted in the sorter order

        # Keep moving left, pushing each node onto the stack
        # When you reach Node, pop a node. This is the next smallest value
        # Increase n. If n == k, return that nodes'value
        # Move to its right child, then repeat

        stack = []
        currentNode = root
        n = 0
        while stack or currentNode is not None:
            #Push all the left nodes into the stack
            #Inner loop to keep moving left before popping
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left


            element = stack.pop()
            n += 1

            if k == n:
                return element.val
            #CurrentNode is None here because it keeps moving Left
            currentNode = element.right
        return 0
        