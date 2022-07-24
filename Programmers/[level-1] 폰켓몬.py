def solution(nums):
    nums_set = set(nums)
    answer = min(len(nums)//2, len(nums_set))
    return answer