def solution(n, times):
    answer = 0
    times.sort()
    def binary_search(r_s, r_e, times, n):
        if r_s>=r_e:
            return r_s
        half = (r_s + r_e)//2
        cnt = [half//i for i in times]
        s = sum(cnt)
        if s>=n:
            return binary_search(r_s, half, times, n)
        else:
            return binary_search(half+1, r_e, times, n)
        
    answer = binary_search(1, times[0]*n+1, times, n)
    return answer