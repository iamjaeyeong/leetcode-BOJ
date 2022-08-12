import sys
input = sys.stdin.readline
total = int(input())
n = int(input())
for i in range(n):
    price, num = map(int, input().split())
    total -= price * num
print("Yes" if total==0 else "No")