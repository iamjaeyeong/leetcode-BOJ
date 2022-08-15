import sys
from collections import deque
input = sys.stdin.readline

singer, pd = list(map(int, input().split()))


orders = []
orders_set = []
total =[0 for i in range(singer)]
for i in range(pd):
    order = list(map(int, input().split()))[1:]
    orders.append(deque(order))
    orders_set.append(set(order))
    for j in order:
        total[j-1] = 1

last = []
for i in range(len(total)):
    if total[i]==0:
        last.append(i)
    
answer = []
is_invalid = 0
while len(answer)!=(singer-len(last)):
    candidates = set()
    candidates_lst = []
    for i in range(len(orders)):
        if len(orders[i])>=1:
            candidate = orders[i].popleft()
            orders_set[i].discard(candidate)
            candidates.add(candidate)
            candidates_lst.append(candidate)
        else:
            candidates_lst.append(None)
    head = []
    for candidate in candidates:
        is_head = 1
        for i in range(len(orders)):
            if candidate in orders_set[i]:
                is_head = 0
                break
        if is_head:
            head.append(candidate)
    if len(head)==0:
        is_invalid = 1
        break
    answer.extend(head)
    
    for i in head:
        for j in range(len(candidates_lst)):
            if i==candidates_lst[j]:
                candidates_lst[j] = None
    for i in range(len(candidates_lst)):
        if candidates_lst[i]==None:
            continue
        else:
            orders_set[i].add(candidates_lst[i])
            orders[i].appendleft(candidates_lst[i])
    
    
    
if is_invalid:
    print(0)
else:
    for i in answer:
        print(i)
    for i in last:
        print(i+1)

        