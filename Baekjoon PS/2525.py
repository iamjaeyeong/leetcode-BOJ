a, b=map(int, input().split())
c=int(input())
a, b=(a, b+c) if b+c<60 else ((a+(b+c)//60)%24, (b+c)%60)
print(a, b)