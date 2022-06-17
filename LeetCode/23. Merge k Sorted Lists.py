class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in lists:
            while i:
                heapq.heappush(heap, i.val)
                i = i.next
                    
        ret = ListNode()
        tmp = ret
        while heap:
            ret.next = ListNode()
            ret = ret.next
            ret.val = heapq.heappop(heap)

            
        return tmp.next
                    