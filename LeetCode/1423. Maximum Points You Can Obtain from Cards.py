class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        forward = [0]
        backward = [0]
        
        f, b, ret = 0, 0, -1
        for i in range(k):
            f += cardPoints[i]
            forward.append(f)
            
        for i in range(len(cardPoints)-1, len(cardPoints)-1-k, -1):
            b += cardPoints[i]
            backward.append(b)
        
        print(forward, backward)
        for i in range(k+1):
            if forward[i]+backward[k-i]>ret:
                ret = forward[i]+backward[k-i]
        
        return ret