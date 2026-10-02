# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using Depth First Search
# Walk through every node of the main tree using DFS starting with root
# At each node, check if the subtree starting here is exactly the same as the subroot

# For every node in the big tree
# If value matches subroot'root, we can both the subtrees fully
# If they are identical, subroot is subtree
# Otherwise continue searching left and right

#Edge case
# What would happen if both trees were null, then they would be the same tree
# IsSubtree: a null subtree is a subtree of another null,
#If S is empty and T is not empty, then it is  not a subtree
# If subtree is null and root is not null, then it is a subtree
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Base Case, if the subtree is empty, then it will be a subtree of the other tree, but the opposite will return false, T a
        if subRoot is None:
            return True
        if root is None:
            return False

        #Want to compare both of the tree
        if self.isSameTree(root, subRoot):
            return True
        
        #Compare subRoot to the left or right of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def isSameTree(self, treeA, treeB):
        #If we are given like empty trees, then they are the same tree technically
        if treeA is None and treeB is None:
            return True

        if treeA is None or treeB is None:
            return False

        if treeA.val != treeB.val:
            return False
        
        leftSide = self.isSameTree(treeA.left, treeB.left)
        rightSide = self.isSameTree(treeA.right, treeB.right)
        return leftSide and rightSide



        