chess = list(map(int, input().split()))

standard = [1, 1, 2, 2, 2, 8]
answer = [i-j for i, j in zip(standard, chess)]
print(answer)