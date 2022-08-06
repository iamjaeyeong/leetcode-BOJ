class Solution:
    def canJump(self, nums) -> bool:
        available = 0
        
        for i in range(len(nums)):
            if available>=i:
                available = max(available, i+nums[i])
                        
        return True if available>=len(nums)-1 else False