import sys
input=sys.stdin.readline

n=int(input())

dp={}

# 2k+1 --> k square + k+1 square
# 2k -->  k square + 2*k*k-1

def pib(n, dp):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    if n in dp:
        return dp[n]
    else:
        if n%2:
            dp[n]=(pow(pib(n//2, dp), 2) + pow(pib(n//2+1, dp),2)) % 1000000007
            return dp[n]
        else:
            dp[n]=(pow(pib(n//2, dp), 2) + 2 * pib(n//2, dp) * pib(n//2-1, dp)) % 1000000007
            return dp[n]

print(pib(n, dp))