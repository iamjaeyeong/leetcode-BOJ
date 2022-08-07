def solution(numbers, target):
    answer = 0
    dp = {numbers[0]:1, numbers[0]*(-1):1}
    for i in range(1, len(numbers)):
        tmp = {}
        for k, v in dp.items():
            if k+numbers[i] in tmp:
                tmp[k+numbers[i]] += v
            else:
                tmp[k+numbers[i]] = v
                
            if k-numbers[i] in tmp:
                tmp[k-numbers[i]] += v
            else:
                tmp[k-numbers[i]] = v
                
        dp = tmp
        
    return dp[target] if target in dp else 0
