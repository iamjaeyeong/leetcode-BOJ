def solution(n):
    answer = ''
    m = 3
    digit = 1
    s = [0]
    while 1:
        if m>=n:
            break
        else:
            p = pow(3, digit)
            s.append(p+s[-1])
            digit += 1
            m += p*3
    nums = ["1", "2", "4"]
    for i in range(digit-1, -1, -1):
        unit = pow(3, i)
        idx = (n-s[i]-1)//unit
        answer += nums[idx]
        n -= unit*(idx+1)
        
    return answer