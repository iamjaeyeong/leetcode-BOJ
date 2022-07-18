def solution(numbers):
    answer = 0
    check = [1 for i in range(10)]
    for n in numbers:
        check[n] = 0
    for i in range(10):
        if check[i]:
            answer += i
    return answer