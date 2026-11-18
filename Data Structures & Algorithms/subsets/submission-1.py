class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            #Explore the left subtree
            subset.append(nums[i])
            dfs(i + 1)

            #If it is not, then you go back and pop the current one
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
