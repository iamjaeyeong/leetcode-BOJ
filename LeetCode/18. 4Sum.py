class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        def binary_search(lst, s, e, find):
            r = -1
            while 1:
                if s>=e:
                    break
                
                mid = (s+e)//2
                if find>lst[mid]:
                    s = mid+1
                elif find==lst[mid]:
                    r = mid
                    break
                else:
                    e = mid
            return r
        ret = []
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j!= i+1 and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1, len(nums)-1):
                    if k!=j+1 and nums[k]==nums[k-1]:
                        continue
                    three = nums[i]+nums[j]+nums[k]
                    p = binary_search(nums, k+1, len(nums), target-three)
                    if p!=-1:
                        ret.append([nums[i], nums[j], nums[k], nums[p]])
        return ret
                        
        