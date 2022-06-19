# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        tokens = []
        token = []
        cnt = 0
        
        h = head
        while 1:
            if cnt==k:
                cnt = 0
                tokens.append(token)
                token = []
            if h==None:
                tail = token
                break
            token.append(h)
            cnt += 1
            h = h.next
        
        for i in range(len(tokens)):
            token = tokens[i]
            for j in range(len(token)-1, 0, -1):
                token[j].next = token[j-1]
            if len(tokens)>i+1:
                token[0].next = tokens[i+1][-1]
            else:
                if tail:
                    token[0].next = tail[0]
                else:
                    token[0].next = None
                    
        if tokens:
            return tokens[0][-1]
        else:
            return tail[0]