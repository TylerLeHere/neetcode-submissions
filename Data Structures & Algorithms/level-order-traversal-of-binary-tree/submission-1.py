# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Breath First Search
        # Intuition Level order traversal visits a tree level by level, from left to right
        # BFS fits because it processes nodes in the order they appear using a queue


        #Key approach:
        # Push the root into the queue
        # Repeatedly remove nodes from the queue, these from the current level
        # Add their children into the queue to form the next level
        # Continue until the queue is empty

        result = []
        myQueue = collections.deque()
        myQueue.append(root)

        while myQueue:
            length = len(myQueue)
            level = []
            for i in range(length):
                node = myQueue.popleft()
                if node:
                    level.append(node.val)
                    #Add whatever current to the queue
                    myQueue.append(node.left)
                    myQueue.append(node.right)
            if level:
                result.append(level)
        return result
        
                


        