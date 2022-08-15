def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    token1 = {}
    token2 = {}
    
    for i in range(len(str1)-1):
        if ord(str1[i])<97 or ord(str1[i])>122 or ord(str1[i+1])<97 or ord(str1[i+1])>122:
            continue
        else:
            token = str1[i:i+2]
            if token in token1:
                token1[token] += 1
            else:
                token1[token] = 1
    
    for i in range(len(str2)-1):
        if ord(str2[i])<97 or ord(str2[i])>122 or ord(str2[i+1])<97 or ord(str2[i+1])>122:
            continue
        else:
            token = str2[i:i+2]
            if token in token2:
                token2[token] += 1
            else:
                token2[token] = 1
    
    intersection = set(token1.keys()).intersection(token2.keys())
    intersection_cnt = 0
    
    for token in intersection:
        intersection_cnt += min(token1[token], token2[token])
        
    total_cnt = sum(token1.values()) + sum(token2.values())

    if total_cnt==0:
        return 65536
    return int(intersection_cnt / (total_cnt-intersection_cnt) * 65536)