import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

front = nums[:int(len(nums)//2)]
back = nums[int(len(nums)//2):]
back = [i*(-1) for i in back]

front_sums = [0]
back_sums = [0]

for i in front:
    new = []
    for j in front_sums:
        new.append(i+j)
    for j in new:
        heapq.heappush(front_sums, j)
        
for i in back:
    new = []
    for j in back_sums:
        new.append(i+j)
    for j in new:
        heapq.heappush(back_sums, j)
answer = 0

front_sums_cnt = [[heapq.heappop(front_sums), 1]]
back_sums_cnt = [[heapq.heappop(back_sums)*(-1), 1]]

while front_sums:
    p = heapq.heappop(front_sums)
    if front_sums_cnt[-1][0]==p:
        front_sums_cnt[-1][1] += 1
    else:
        front_sums_cnt.append([p, 1])

while back_sums:
    p = heapq.heappop(back_sums) * (-1)
    if back_sums_cnt[-1][0]==p:
        back_sums_cnt[-1][1] += 1
    else:
        back_sums_cnt.append([p, 1])

is_bigger = 1
is_smaller = 1
p1 = 0
p2 = 0

while 1:
    if p1==len(front_sums_cnt) or p2==len(back_sums_cnt):
        break      
    else:
        if front_sums_cnt[p1][0] + back_sums_cnt[p2][0] > m:
            p2 += 1
        elif front_sums_cnt[p1][0] + back_sums_cnt[p2][0] == m:
            answer += front_sums_cnt[p1][1] * back_sums_cnt[p2][1]
            p1 += 1
        else:
            p1 += 1
    
            
if m==0:
    answer -= 1
print(answer)
            
    
    
        