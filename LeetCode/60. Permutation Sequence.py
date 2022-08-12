class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [0, 1]
        for i in range(2, n):
            factorial.append(factorial[-1]*i)

        check = [0 for i in range(n)]
        answer = ""
        k -= 1
        
        for i in range(n-1, 0, -1):
            cnt = k//factorial[i]
            k -= factorial[i]*cnt
            idx = 0

            while 1:
                if check[idx]==0:
                    cnt -= 1
                if cnt>=0:
                    idx += 1
                else:
                    break
                    
            answer += str(idx+1)
            check[idx] = 1

        for i in range(n):
            if check[i]==0:
                answer += str(i+1)
                break
        return answer