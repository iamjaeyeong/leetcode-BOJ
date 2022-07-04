def solution(id_list, report, k):
    id_dict = {id_:i for i, id_ in enumerate(id_list)}
    check = [[0 for j in range(len(id_list))] for i in range(len(id_list))]
    answer = [0 for i in range(len(id_list))]

    for i in report:
        reporter, reported = i.split()
        check[id_dict[reported]][id_dict[reporter]] = 1
    
    suspended = []
    for i in range(len(check)):
        cnt = 0
        for j in check[i]:
            if j:
                cnt += 1
        if cnt>=k:
            suspended.append(i)
            
    for i in suspended:
        for j in range(len(check[i])):
            if check[i][j]:
                answer[j] += 1
    
    return answer