class Solution:
    def checkPossibility(self, nums) -> bool:
        def check(nums):
            ret = True
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    ret = False
                    break
            return ret
        
        cnt = 0
        is_false = False
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                tmp = nums[i+1]
                nums[i+1] = nums[i]
                back = check(nums)
                
                nums[i+1] = tmp
                if i==0:
                    nums[i] = 0
                else:
                    nums[i] = nums[i-1]
                front = check(nums)
                
                if not(back or front):
                    is_false = True
                break
                
                    
                
        return False if is_false else True