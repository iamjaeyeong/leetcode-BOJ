class Solution:    
    def threeSum(self, nums):
        if len(nums)<3:
            return []
        
        def binary_search(lst, s, e, find):
            k = -1
            while 1:
                if s>=e:
                    break
                mid = (s+e)//2
                if find>lst[mid]:
                    s = mid+1
                elif find<nums[mid]:
                    e = mid
                else:
                    k = mid
                    break
            return k
        
        ret = []
        nums.sort()
        
        pair = []
        set_nums = []
        
        idx = 0
        while idx<len(nums):
            set_nums.append(nums[idx])
            if idx+1<len(nums) and nums[idx+1]==nums[idx]:
                if nums[idx]==0 and idx+2<len(nums) and nums[idx+2]==nums[idx]:
                    ret.append([0, 0, 0])
                else:
                    pair.append(nums[idx])
                while idx<len(nums):
                    if idx+1<len(nums) and nums[idx]!=nums[idx+1]:
                        break
                    else:
                        idx+=1
            idx+=1  
            
        nums = set_nums

        for i in range(len(nums)):
            for j in range(i+2, len(nums)):
                k = binary_search(nums, i+1, j, (nums[i]+nums[j])*(-1))
                if k!=-1:
                    ret.append([nums[i], nums[k], nums[j]]) 
                    
        for i in pair:
            k = binary_search(nums, 0, len(nums), i*(-2))
            if nums[k]!=0 and k!=-1:
                ret.append([i, i, nums[k]])
        
        return ret