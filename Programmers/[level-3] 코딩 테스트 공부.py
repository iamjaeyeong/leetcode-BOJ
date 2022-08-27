def solution(alp, cop, problems):
    answer = 0
#     row = alp, col = cop
    inf = 500
    
    mx_al = max(max(i[0] for i in problems) + 1, alp+1)
    mx_co = max(max(i[1] for i in problems) + 1, cop+1)
    dp = [[0 for i in range(mx_co)]for j in range(mx_al)]
    for al in range(alp, mx_al):
        for co in range(cop, mx_co):
            dp[al][co] = inf
    
    for al in range(alp, mx_al):
        for co in range(cop, mx_co):
            if al==alp and co==cop:
                dp[al][co] = 0
            elif al==alp:
                dp[al][co] = min(dp[al][co], dp[al][co-1] + 1)
            elif co==cop:
                dp[al][co] = min(dp[al][co], dp[al-1][co] + 1)
            else:
                dp[al][co] = min(dp[al][co], dp[al][co-1] + 1, dp[al-1][co] + 1)
            for prob in problems:
                if al>=prob[0] and co>=prob[1]:
                    row = min(mx_al-1, al+prob[2])
                    col = min(mx_co-1, co+prob[3]) 
                    dp[row][col] = min(dp[row][col], dp[al][co]+prob[4])
    
    answer = dp[-1][-1]

    
    return answer