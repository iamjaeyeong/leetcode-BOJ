def solution(lottos, win_nums):
    cnt, zero = 0, 0
    
    for i in range(len(lottos)):
        if lottos[i]==0:
            zero += 1
            continue
        for j in range(len(win_nums)):
            if lottos[i]==win_nums[j]:
                cnt += 1
                break
    
    mn = cnt
    mx = cnt + zero

    answer = [min(6, 7-mx), min(6, 7-mn)]
    return answer