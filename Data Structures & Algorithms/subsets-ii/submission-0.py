class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Problem subsets 2
        #How can prevent duplicate
        #What the right side should represent is all the possible subsets that does not include any two values
        #What we choose to skip this 2, we should try to skip all 2, but gotta make sure it is sorted first, sort it ourself, nlogn times, time complexity of this solution is n*2^n
        res = []
        nums.sort()

        #i: index that we are at from the nums array, what is the current subset looking like so far
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            #What is the recursive case, 2 decisions to make
            # All subsets include number[i], the number that we are at
            # The other cause is all subset that does not include the num of i

            #First one
            subset.append(nums[i])
            #Do back tracking call passing in the next index
            backtrack(i + 1, subset) # Taking care of all subsets inlcude this number
            
            #Before we generate all subsets not including that number
            #We should proabbly remove from the subset that val that we added to it
            subset.pop()
            #All subsets that don't include nums[i], 
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i = i + 1
            #Run the backtracking again, it is the case that adding the empty array to the results
            backtrack(i + 1, subset)
        
        backtrack(0,[])
        return res

                            

            
            

         



         
        