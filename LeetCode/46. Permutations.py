class Solution:
    def permute(self, nums):
        def dfs(nums, check, p, depth, ret=[]):
            if len(nums)==depth:
                ret.append(p)
            else:
                for i in range(len(check)):
                    if check[i]:
                        continue
                    else:
                        check[i] = 1
                        dfs(nums, check, p+[nums[i]], depth+1, ret=ret)
                        check[i] = 0
        ret = []
        dfs(nums, [0 for i in range(len(nums))], [], 0, ret=ret)
        return ret