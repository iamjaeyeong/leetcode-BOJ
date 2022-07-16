def solution(numbers, hand):
    answer = ''
    left_pos = [3, 0]
    right_pos = [3, 2]
    
    def distance(pos1, pos2):
        delta_x = abs(pos1[1] - pos2[1])
        delta_y = abs(pos1[0] - pos2[0])
        return delta_x + delta_y
    
    for n in numbers:
        if n==1 or n==4 or n==7:
            left_pos = [(n-1)//3, 0]
            answer += "L"
        elif n==3 or n==6 or n==9:
            right_pos = [(n-3)//3, 2]
            answer += "R"
        else:
            if n==0:
                pos = [3, 1]
            else:
                pos = [(n-2)//3, 1]
            left_dis = distance(left_pos, pos)
            right_dis = distance(right_pos, pos)
            if left_dis<right_dis:
                left_pos = pos
                answer += "L"
            elif left_dis>right_dis:
                right_pos = pos
                answer += "R"
            else:
                if hand=="left":
                    left_pos = pos
                    answer += "L"
                else:
                    right_pos = pos
                    answer += "R"
                
    return answer