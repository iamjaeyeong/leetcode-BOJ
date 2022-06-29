class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rev = 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                rev = 0
                break
        
        if rev:
            nums.sort()
        else:
            nums_sort = [i for i in nums]
            nums_sort.sort()
            stack = []
            mx = nums[-1]
            stack.append(nums[-1])

            
            for i in range(len(nums)-2, -1, -1):
                if mx>nums[i]:
                    mn = mx
                    for j in stack:
                        if j>nums[i] and j<mn:
                            mn = j
                    nums[i] = mn
                    tmp = i
                    break           
                else:
                    stack.append(nums[i])
                    mx = nums[i]
            
            idx = tmp+1
            for i in range(idx):
                for j in range(len(nums_sort)):
                    if nums[i]==nums_sort[j]:
                        nums_sort[j] = None
                        break
            print(nums_sort)
            for i in nums_sort:
                if i!=None:
                    nums[idx] = i
                    idx += 1