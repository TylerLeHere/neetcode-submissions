class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 0:
            return [[]]
        #The main idea is to arrange the remaining numbers first, then insert the first number into very every possible solution
        permutations = self.permute(nums[1:])
        #Take each arragement and inset the first one everywhere
        for eachPermutation in permutations:
            for index in range(len(eachPermutation) + 1):
                copy = eachPermutation[:]
                copy.insert(index, nums[0])
                result.append(copy)
        
        return result

        