def solution(record):
    info = dict()
    logs = [list(r.split(" ")) for r in record]
    answer = []
    for log in logs:
        if log[0]=="Leave":
            continue
        info[log[1]] = log[2]
        
    for log in logs:
        if log[0]=="Enter":
            answer.append(f"{info[log[1]]}님이 들어왔습니다.")
        elif log[0]=="Leave":
            answer.append(f"{info[log[1]]}님이 나갔습니다.")

    return answer