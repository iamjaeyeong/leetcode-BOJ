class Solution:
    def jump(self, nums) -> int:
        import math
        inf = math.inf
        dp = [inf for i in range(len(nums))]
        dp[0] = 0
        
        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                if i+j>=len(dp):
                    break
                dp[i+j] = min(dp[i+j], dp[i]+1)
        
        return dp[-1]