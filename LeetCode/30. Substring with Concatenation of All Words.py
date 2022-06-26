from collections import deque

class Solution:
    def findSubstring(self, s: str, words):
        def check(cnt, cmp):
            r = True
            for key, value in cmp.items():
                if cnt[key]!=value:
                    r = False
                    break
            return True if r else False
                
        
        words_set = set(words)
        word_count = {word:0 for word in words_set}
        unit = (len(words)-1)*len(words[0])
        ret = []
        
        for word in words:
            word_count[word] += 1
            
        for i in range(len(words[0])):
            deq = deque()
            for j in range(i, len(s), len(words[0])):
                if s[j:j+len(words[0])] in words_set:
                    deq.append(s[j:j+len(words[0])])
                else:
                    deq = deque()
                    continue
                
                if len(deq)==len(words):
                    cmp = {word:0 for word in words_set}
                    for k in deq:
                        cmp[k] += 1
                    if check(word_count, cmp):
                        ret.append(j-unit)
                    
                elif len(deq)==len(words)+1:
                    cmp[deq.popleft()] -= 1
                    cmp[deq[-1]] += 1
                    if check(word_count, cmp):
                        ret.append(j-unit)
                        
        return ret