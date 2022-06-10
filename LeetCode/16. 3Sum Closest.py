class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        def binary_search(lst, s, e, find):
            while 1:
                if s+1==e:
                    k = s
                    break
                mid = (s+e)//2
                if find>lst[mid]:
                    s = mid
                elif find<lst[mid]:
                    e = mid
                else:
                    k = mid
                    break
            return k
        
        ret = 100000
        for i in range(len(nums)):
            for j in range(i+2, len(nums)):
                k = binary_search(nums, i+1, j, target-(nums[i]+nums[j]))
                if abs(target-ret)>abs(target-(nums[i]+nums[j]+nums[k])):
                    ret = (nums[i]+nums[j]+nums[k])
        
        return ret