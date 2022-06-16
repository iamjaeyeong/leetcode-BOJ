# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        tmp = ret

        while 1:
            if list1==None or list2==None:
                if list1==None:
                    while list2:
                        ret.next = list2
                        ret = ret.next
                        list2 = list2.next
                    break
                elif list2==None:
                    while list1:
                        ret.next = list1
                        ret = ret.next
                        list1 = list1.next
                    break
                else:
                    break
            if list1.val<list2.val:
                ret.next = list1
                list1 = list1.next
            else:
                ret.next = list2
                list2 = list2.next
            ret = ret.next
        return tmp.next
            