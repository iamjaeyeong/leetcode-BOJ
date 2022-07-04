class Solution:
    def searchRange(self, nums, target: int):
        if nums==[]:
            return [-1, -1]
        def binary_search(nums, s, e, f, ret_lst=0):
            if s+1>=e:
                if nums[s]!=f:
                    s = -1
                return [s, s] if ret_lst==0 else s
            mid = (s+e)//2
            if nums[mid]>f:
                return binary_search(nums, s, mid, f, ret_lst=ret_lst)
            elif nums[mid]<f:
                return binary_search(nums, mid, e, f, ret_lst=ret_lst)
            else:
                if ret_lst==0:
                    if mid==0 or nums[mid-1]!=f:
                        left = mid
                    else:
                        left = binary_search(nums, s, mid, f, ret_lst=1)
                    if mid==len(nums)-1 or nums[mid+1]!=f:
                        right = mid
                    else:
                        right = binary_search(nums, mid, e, f, ret_lst=2)
                    return [left, right]
                elif ret_lst==1:
                    if mid==0 or nums[mid-1]!=f:
                        left = mid
                    else:
                        left = binary_search(nums, s, mid, f, ret_lst=1)
                    return left
                else:
                    if mid==len(nums)-1 or nums[mid+1]!=f:
                        right = mid
                    else:
                        right = binary_search(nums, mid, e, f, ret_lst=2)
                    return right

        return binary_search(nums, 0, len(nums), target)