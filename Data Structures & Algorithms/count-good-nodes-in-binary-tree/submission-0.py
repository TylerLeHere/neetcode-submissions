# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Algo
        # Start DFS from the root and store the root's val as the current max       
        result = self.dfs(root, root.val) 
        return result

    def dfs(self, currentNode: TreeNode, maxValSoFar: int) -> int:
        #Think about the edge case first, 
        if currentNode is None:
            return 0
        
        count = 0
        if currentNode.val >= maxValSoFar:
            count += 1
        maxValSoFar = max(maxValSoFar, currentNode.val)
        leftCount = self.dfs(currentNode.left, maxValSoFar)
        rightCount = self.dfs(currentNode.right, maxValSoFar)

        return count + leftCount + rightCount

