def solution(s):
    idx = 0
    answer = ""
    while idx<len(s):
        if 48<=ord(s[idx])<=57:
            answer += s[idx]
            idx += 1
        else:
            if s[idx]=="z":
                idx += 4
                answer += "0"
            elif s[idx]=="o":
                idx += 3
                answer += "1"
            elif s[idx]=="e":
                idx += 5
                answer += "8"
            elif s[idx]=="n":
                idx += 4
                answer += "9"
            elif s[idx]=="t":
                if s[idx+1]=="w":
                    idx += 3
                    answer += "2"
                else:
                    idx += 5
                    answer += "3"
            elif s[idx]=="f":
                if s[idx+1]=="o":
                    idx += 4
                    answer += "4"
                else:
                    idx += 4
                    answer += "5"
            else:
                if s[idx+1]=="i":
                    idx += 3
                    answer += "6"
                else:
                    idx += 5
                    answer += "7"

    return int(answer)