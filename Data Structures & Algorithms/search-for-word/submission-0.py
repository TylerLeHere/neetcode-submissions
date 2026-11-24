class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #One thing I like to do
        # Recursive DFS

        #Getting the dimensions
        ROWS = len(board)
        COLS = len(board[0])

        #Can't revisit the same char twice within our path, so use set to add all cur val from our board within our path
        path = set()

        #path in the position and current char within our target word we are looking for
        def dfs(r, c, i):
            if i == len(word):
                #We found the word, return true
                return True
            
            #Out of bound of the entire board
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False
            
            #We found the char we are looking for
            path.add((r,c))
            #Contine dfs
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1)or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1)
            )
            #Only need to find target one one signle time
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                #Run dfs
                if dfs(r, c, 0):
                    return True
        
        return False





        