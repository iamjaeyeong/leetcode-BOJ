class Solution:
    def combinationSum(self, candidates, target: int):
        dp = {i:[] for i in range(target+1)}
        
        for candidate in candidates:
            for i in range(len(dp)):
                if dp[i] and i+candidate<=target:
                    dp[i+candidate].extend([j+[candidate] for j in dp[i]])
            cnt = 1
            while cnt*candidate<=target:
                dp[cnt*candidate].append([candidate]*cnt)
                cnt += 1

        return dp[target]
        