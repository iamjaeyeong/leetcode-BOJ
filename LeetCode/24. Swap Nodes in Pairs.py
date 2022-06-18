# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):   
        head = ListNode(val=0, next=head)
        ret = head
        
        while 1:
            h1 = head.next
            if h1==None:
                break
                
            h2 = h1.next
            if h2==None:
                break
            h3 = h2.next
            
            head.next = h2
            h2.next = h1
            h1.next = h3
            
            head = h1
            
        return ret.next