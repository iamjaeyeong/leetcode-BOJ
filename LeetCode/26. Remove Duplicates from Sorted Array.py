class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        tmp = -101
        while i<len(nums):
            if nums[i]>tmp:
                nums[j] = nums[i]
                tmp = nums[j]
                j += 1
            i += 1
        return j