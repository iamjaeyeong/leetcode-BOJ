def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    one_score = 0
    two_score = 0
    three_score = 0
    
    for i, j in enumerate(answers):
        if one[i%5]==j:
            one_score += 1
        if two[i%8]==j:
            two_score += 1
        if three[i%10]==j:
            three_score += 1
    
    highest = max(one_score, two_score, three_score)
    if one_score==highest:
        answer.append(1)
    if two_score==highest:
        answer.append(2)
    if three_score==highest:
        answer.append(3)
    
    return answer

