class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            
            #i: maintain which candiates still allow to choose, curr: a list tells us what values added so far for the curr combincation, total
            if total == target:
                res.append(curr[:]) # Want to copy because we can continue to use
                return
            
            # i out of bound meaning can not choose any other candiate
            if i >= len(nums) or total > target:
                return # can not find the combination

            #include the values at
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            #Not ever including that candiate
            dfs(i + 1, curr, total) # total stays the same because we did not add value to it
        dfs(0, [], 0) #Empty index
        return res





        