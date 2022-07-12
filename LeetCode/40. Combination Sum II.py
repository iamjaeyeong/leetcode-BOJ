from collections import Counter

class Solution:
    def combinationSum2(self, candidates, target: int):    
        dp = {i:[] for i in range(target+1)}
        dp[0].append([])
        
        cnt = {i:0 for i in candidates}
        for c in candidates:
            cnt[c] += 1
            
        candidates = set(candidates)
        
        for c in candidates:
            for i in range(target+1, -1, -1):
                for rep in range(1, cnt[c]+1):
                    if rep*c+i>target:
                        continue
                    for lst in dp[i]:
                        dp[rep*c+i].append([c]*rep+lst)
        
        return dp[target]
   
                    