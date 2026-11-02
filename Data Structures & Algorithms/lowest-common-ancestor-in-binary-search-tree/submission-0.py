# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Given a binary search tree, root on the left is less than the right

        currentNode = root
        while currentNode:
            #If both p and q are less than currentNode, both move left
            if p.val < currentNode.val and q.val < currentNode.val:
                #currentNode should move left
                currentNode = currentNode.left
            elif p.val > currentNode.val and q.val > currentNode.val:
                #currentNode should move right
                currentNode = currentNode.right
            else:
                return currentNode


        