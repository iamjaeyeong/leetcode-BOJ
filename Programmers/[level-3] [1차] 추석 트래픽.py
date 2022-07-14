def solution(lines):
    def to_int(end_time):
        ret = 0
        ret += int(end_time[0:2])*1000*60*60
        ret += int(end_time[3:5])*1000*60
        ret += int(end_time[6:8])*1000
        ret += int(end_time[9:])
        return ret
    
    def to_int2(running_time):
        running_time = running_time[:-1]
        ret = 0
        ret += int(running_time[0])*1000
        if len(running_time)>2:
            ret += int(running_time[2:])
        return ret
    
    start = []
    end = []
    
    for log in lines:
        date, end_time, running_time = list(log.split(" "))
        end_time = to_int(end_time)
        running_time = to_int2(running_time)
        start.append(end_time-running_time+1)
        end.append(end_time)
        
    p1, p2 = 0, 0
    answer = 0
    start.sort()
    
    while 1:
        if p2>=len(start):
            break
        while 1:
            if p2>=len(lines) or start[p2]>=end[p1]+1000:
                break
            p2 += 1
        answer = max(p2-p1, answer)
        p1 += 1

    return answer