def solution(progresses, speeds):
    answer = []
    in_progress = 0
    while 1:
        if in_progress==len(progresses):
            break
        if progresses[in_progress]>=100:
            tmp = 0
            while 1:
                if in_progress<len(progresses) and progresses[in_progress]>=100:
                    tmp += 1
                    in_progress += 1
                else:
                    break
            answer.append(tmp)
        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
            
        
    return answer