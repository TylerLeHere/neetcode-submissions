class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        leftP = 0
        rightP = len(nums) - 1

        while leftP <= rightP:
            middleIndex = (leftP +rightP) // 2
            res = min(res, nums[middleIndex])
            if nums[leftP] < nums[rightP]:
                res = min(res, nums[leftP])
                break

            if nums[middleIndex] >= nums[leftP]:
                #It is part of the rotation, which means the smaller number is on the right
                leftP = middleIndex + 1
            else:
                rightP = middleIndex - 1
        
        return res





        