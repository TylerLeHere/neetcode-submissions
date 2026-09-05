class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        #Find the entrance to the cycle
        slow2 = nums[0]
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow2

