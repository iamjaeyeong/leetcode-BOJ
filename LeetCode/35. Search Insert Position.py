class Solution:
    def searchInsert(self, nums, target: int) -> int:
        def binary_search(nums, s, e, f):
            if s+1>=e:
                if nums[s]<f:
                    return s+1
                return s
            
            mid = (s+e)//2
            if nums[mid]<f:
                return binary_search(nums, mid, e, f)
            elif nums[mid]>f:
                return binary_search(nums, s, mid, f)
            else:
                return mid
            
        return binary_search(nums, 0, len(nums), target)