# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head==None or head.next==None:
            return head
        length = 1
        cnt = head
        while cnt.next:
            cnt = cnt.next
            length += 1
        k %= length
        head_node = head
        next_node = head.next
        for i in range(k):
            first_node = head_node
            while next_node.next:
                head_node = next_node
                next_node = head_node.next
            head_node.next = None
            next_node.next = first_node
            head_node = next_node
        return head_node
    