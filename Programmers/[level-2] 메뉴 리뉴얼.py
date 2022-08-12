def solution(orders, course):
    answer = []
    def get_combination(order, n, k, start, prev, ret):
        if k==n:
            ret.append(prev)
        else:
            for i in range(start, len(order)-n+k+1):
                get_combination(order, n, k+1, i+1, prev+order[i], ret)
    for n in course:
        cnt = {}
        for order in orders:
            order = sorted(order)
            combinations = []
            get_combination(order, n, 0, 0, "", combinations)
            for combination in combinations:
                if combination in cnt:
                    cnt[combination] += 1
                else:
                    cnt[combination] = 1
        if cnt.values():
            mx = max(cnt.values())
        if mx>1:
            for k, v in cnt.items():
                if v==mx:
                    answer.append(k)
    answer.sort()
    return answer