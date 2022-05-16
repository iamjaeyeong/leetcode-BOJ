import sys
input=sys.stdin.readline

n, k=map(int, input().split())

if k>n//2:
    k=n-k

def fast_square(a, p):
	if p<2:
		if p==1:
			return a
		else:
			return 1
	if a>1000000007:
		a=a%1000000007
	if p%2:
		return fast_square(a, p-1)*a
	else:
		return pow(fast_square(a, p//2), 2)%1000000007

a=1
b=1

for i in range(n-k+1, n+1):
	a*=i
	if a>1000000007:
		a=a%1000000007
for i in range(1, k+1):
	b*=i
	if b>1000000007:
		b=b%1000000007


tmp=fast_square(b, 1000000005)
print((a%1000000007)*(tmp%1000000007)%1000000007)
