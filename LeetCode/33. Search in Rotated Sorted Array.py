class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums, s, e):
            if s+1>=e:
                if nums[s-1]>nums[s]:
                    return s
                else:
                    return s+1
            mid = (s+e)//2
            if nums[s-1]>nums[s]:
                return s
            if nums[s]<nums[mid]:
                return find_pivot(nums, mid+1, e)
            else:
                return find_pivot(nums, s, mid)
        
        def binary_search(nums, s, e, f):
            if s+1>=e:
                return s
            mid = (s+e)//2
            if nums[mid]>f:
                return binary_search(nums, s, mid, f)
            elif nums[mid]<f:
                return binary_search(nums, mid+1, e, f)
            else:
                return mid
            
        pivot = find_pivot(nums, 0, len(nums))
        
        if pivot==0:
            s = 0
            e = len(nums)
        elif nums[0]>target:
            s = pivot
            e = len(nums)           
        else:
            s = 0
            e = pivot
        
        idx = binary_search(nums, s, e, target)
        if idx==len(nums):
            return -1
        return idx if nums[idx]==target else -1