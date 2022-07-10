class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        base = "11"
        n -= 1
        
        def recursion(n, string):
            if n==1:
                return string
            else:
                ret = ""
                prev = string[0]
                cnt = 1
                for i in range(1, len(string)):
                    if string[i]==prev:
                        cnt += 1
                    else:
                        ret += (str(cnt) + prev)
                        prev = string[i]
                        cnt = 1

                ret += (str(cnt) + prev)
                return recursion(n-1, ret)
        
        return recursion(n, base)
    
    
a = Solution()
print(a.countAndSay(29))