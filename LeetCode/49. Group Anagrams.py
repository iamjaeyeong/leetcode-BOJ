class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for s in strs:
            cnt = [0 for i in range(26)]
            for c in s:
                cnt[ord(c)-97] += 1
            
            cnt_s = ""
            for c in cnt:
                cnt_s += str(c)+","
                
            if cnt_s in d:
                d[cnt_s].append(s)
            else:
                d[cnt_s] = [s]
        
        answer = []
        for i, j in d.items():
            answer.append(j)
        return answer