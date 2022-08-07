def solution(N, number):
    def calculate(a, b):
        return a+b, abs(a-b), a*b, a//b
    
    step = 1

    dp = set()
    dp.add(N)
    unit = [[None], []]
    digit = [None, 1, 11, 111, 1111, 11111, 111111, 1111111, 11111111]
    
    while 1:
        if step>7:
            break
        
        new = []
        unit[step].append(digit[step]*N)
        dp.add(digit[step]*N)   
        for i in range(step, step//2, -1):
            for j in unit[i]:
                for k in unit[step-i+1]:
                    for p in calculate(j, k):
                        if p in dp or p<=0:
                            continue
                        else:
                            new.append(p)
                            dp.add(p)
        step += 1
        unit.append(new)
        
    for i in range(1, 9):
        for j in unit[i]:
            if j==number:
                return i
    return -1
