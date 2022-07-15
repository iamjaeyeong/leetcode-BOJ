class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num2)>len(num1):
            num1, num2 = num2, num1
        num1 = int(num1)
        ret = []
        for i in range(1, len(num2)+1):
            digit = int(num2[-1*i])
            ret.append(str(digit*num1)+"0"*(i-1))
        
        def str_sum(s1, s2):
            idx1 = len(s1)-1
            idx2 = len(s2)-1
            up = 0
            s1 = [int(i) for i in s1]
            while idx2>-1:
                tmp = s1[idx1] + int(s2[idx2])
                if tmp>9:
                    cnt = 1
                    while 1:
                        if s1[idx1-cnt]<9:
                            s1[idx1-cnt] += 1
                            break
                        else:
                            s1[idx1-cnt] = 0
                            cnt += 1
                    tmp -= 10
                s1[idx1] = tmp
                idx1 -= 1
                idx2 -= 1
            return s1
        
        answer = "0" + ret[-1]
        for i in range(0, len(ret)-1):
            answer = str_sum(answer, ret[i])
        
        answer2 = ""
        s = 0
        if answer[0]=="0" or answer[0]==0:
            s = 1
        for i in range(s, len(answer)):
            answer2 += str(answer[i])
            
        return answer2
        
        