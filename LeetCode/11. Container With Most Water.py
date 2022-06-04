import heapq

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """        
        heap = []
        for i in range(len(height)):
            heapq.heappush(heap, (-1*height[i], i))
          
        v1 = heapq.heappop(heap)
        v2 = heapq.heappop(heap)
        ret = abs(v2[0]*(v1[1]-v2[1]))
        
        while heap:
            v3 = heapq.heappop(heap)
            if v1[1]<=v3[1]<=v2[1] or v2[1]<=v3[1]<=v1[1]:
                continue
            else:
                width = max(abs(v3[1]-v1[1]), abs(v3[1]-v2[1]))
                h = v3[0]
                ret = max(ret, h*width*(-1))
                # v1 v3
                if abs(v3[1]-v1[1]) > abs(v3[1]-v2[1]):
                    v2 = v3
                else:
                    v1 = v3
        
        return ret
                    
            