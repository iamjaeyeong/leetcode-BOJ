class Solution:
    def permuteUnique(self, nums):
        ans = []
        nums.sort()
        def dfs(nums, p, check, ans=ans):
            if len(p)==len(nums):
                ans.append(p)
            else:
                prev = None
                for i in range(len(nums)):
                    if check[i]:
                        continue
                    else:
                        if prev==nums[i]:
                            continue
                        check[i] = 1
                        dfs(nums, p+[nums[i]], check, ans=ans)
                        check[i] = 0
                        prev = nums[i]
        dfs(nums, [], [0 for i in range(len(nums))], ans=ans)
        return ans
        