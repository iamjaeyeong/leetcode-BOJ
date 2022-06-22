class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        cnt = [0 for i in range(20001)]
        for i in nums:
            cnt[i+10000] += 1
        
        idx = 20000
        while 1:
            if cnt[idx]>=k:
                break
            else:
                k -= cnt[idx]
                idx -= 1
                
        return idx-10000