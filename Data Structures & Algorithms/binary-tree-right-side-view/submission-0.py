# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Know about BFS, level-order traversal using a queue to process nodes level by level
        result = []
        #Returning 
        myQueue = deque()
        myQueue.append(root)

        while myQueue:
            #Want to loop through each level of the tree based on the queue
            lengthQueue = len(myQueue)
            rightSide = None

            for i in range(lengthQueue):
                #Loop through each level
                node = myQueue.popleft()
                #if there is a node
                if node:
                    #Get the children and appeand to the queue
                    rightSide = node
                    myQueue.append(node.left)
                    myQueue.append(node.right)
                
            if rightSide:
                result.append(rightSide.val)
        
        return result
                    

            
        