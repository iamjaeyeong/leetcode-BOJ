class Solution:
    def firstMissingPositive(self, nums) -> int:
        check = [0 for i in range(len(nums)+1)]
        
        for i in nums:
            if i>0 and i<=len(nums):
                check[i] = 1
            
        for i in range(1, len(nums)+1):
            if check[i]==0:
                return i
        return len(nums)+1