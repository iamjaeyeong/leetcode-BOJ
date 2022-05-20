class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total=len(num1)+len(num2)
        inf=100000000
        num1.append(inf)
        num2.append(inf)
        p1, p2=-1, -1
        n_iter=total//2 if total%2==1 else total//2-1
        for i in range(n_iter):
            if num1[p1+1]<num2[p2+1]:
                p1+=1
            else:
                p2+=1
        if total%2==1:
            return min (num1[p1+1], num2[p2+1])
        else:
            if num1[p1+1]==inf:
                return (num2[p2+1]+num2[p2+2])/2
            elif num2[p2+1]==inf:
                return (num1[p1+1]+num1[p1+2])/2
            else:
                return min(num1[p1+1]+num2[p2+1],num2[p2+1]+num2[p2+2],num1[p1+1]+num1[p1+2])/2