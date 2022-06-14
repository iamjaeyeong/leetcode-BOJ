# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        l = 0
        tmp = head
        pseudo_head = ListNode(next=head)
        ret = pseudo_head
        while 1:
            if tmp.next==None:
                l += 1
                break
            else:
                tmp = tmp.next
                l += 1
        
        cnt = 0
        while 1:
            if cnt==l-n:
                pseudo_head.next = pseudo_head.next.next
                break
            else:
                pseudo_head = pseudo_head.next
                cnt += 1
        return ret.next