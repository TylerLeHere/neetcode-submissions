class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Only add open paranthesis if open < n
        #Only add a closign paranthesis if closed < open
        #Valid if open == closed == n

        stack = []
        res = []

        def backtracking(open, close):
            if open == close and open == n:
                completedString = "".join(stack)
                res.append(completedString)
                return
            
            if open < n:
                #Add closing paratnthesis
                stack.append("(")
                #Recursively do it again with open increase
                backtracking(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtracking(open, close + 1)
                stack.pop()
        
        backtracking(0, 0)
        return res
        
        

        