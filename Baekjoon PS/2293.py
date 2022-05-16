import sys
input=sys.stdin.readline
n, k=map(int, input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))
amount={i:0 for i in range(k+1)}

amount[0]=1
for i in coins:
    for j in amount:
        a=amount[j]
        if a==0:
            continue
        if j+i>k:
            break
        else:
            amount[j+i]+=a
            
print(amount[k])