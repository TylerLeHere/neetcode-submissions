# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Using recursinve DFS
        # if root is None:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #Using BFS

        if root is None:
            return 0
        
        #Maintain the current level we are at
        level = 0
        q = deque([root])
        #Keep going until the queue is empty

        while q:
            for i in range(len(q)):
                #Traverse the entire level and add the next one
                #For every node from the queue
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return level
