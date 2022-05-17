# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        self.ret=ListNode()
        self.ans=self.ret
        while 1:
            tmp=l1.val+l2.val+self.ans.val
            self.ans.val=tmp%10
            if l1.next==None and l2.next==None:
                break
            elif l1.next==None:
                l1.val=0
                l2=l2.next
            elif l2.next==None:
                l2.val=0
                l1=l1.next
            else:
                l1=l1.next
                l2=l2.next
            if tmp>=10:
                self.ans.next=ListNode(val=1)
            else:
                self.ans.next=ListNode(val=0)
            self.ans=self.ans.next
        if tmp>=10:
            self.ans.next=ListNode(val=1)
        return self.ret
        