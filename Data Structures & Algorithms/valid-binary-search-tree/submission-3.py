# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = self.dfs(root, float("-inf"), float("+inf"))
        return result

    def dfs(self, currentNode, leftBound, rightBound) -> bool:
        #If everything is empty, return true
        if currentNode is None:
            return True
        #If it is not strictly in between, return false
        if currentNode.val <= leftBound or currentNode.val >= rightBound:
            return False

        #Now we want to recursively validate left SubTree and RightSubTree
        left = self.dfs(currentNode.left, leftBound, currentNode.val)
        right = self.dfs(currentNode.right, currentNode.val, rightBound)

        return left and right

        