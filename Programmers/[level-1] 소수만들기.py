def solution(nums):
    answer = 0
    mx = max(nums)
    cnt = [0 for i in range(mx*3)]
    
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                cnt[nums[i]+nums[j]+nums[k]] += 1
    
    def prime(mx):
        lst = [i for i in range(3*mx)]
        for i in range(2, int(pow(mx*3, 1/2))+1):
            tmp = 2
            while 1:
                if tmp*i>=len(lst):
                    break
                lst[i*tmp] = 0
                tmp += 1
        ret = []
        for i, j in enumerate(lst):
            if j:
                ret.append(i)
        return ret
    prime_nums = prime(mx)
    for p in prime_nums:
        answer += cnt[p]

    return answer