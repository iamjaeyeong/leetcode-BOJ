class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(s, n, a, b, p):
            if a==n and b==n:
                p.append(s)
            elif a==n:
                p.append(s+')'*(n-b))
            else:
                generate(s+'(', n, a+1, b, p)
                if a>b:
                    generate(s+')', n, a, b+1, p)
        
        ret = []
        generate("(", n, 1, 0, ret)
        return ret