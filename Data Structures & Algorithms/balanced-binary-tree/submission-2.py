# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.dfs(root)
        if res == -1:
            return False
        return True
    
    def dfs(self, root):
        if root is None:
            return 0
        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)

        if leftHeight == -1 or rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1

        return 1 + max(leftHeight, rightHeight)
        
        