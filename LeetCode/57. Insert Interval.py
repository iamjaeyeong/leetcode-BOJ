class Solution:
    def insert(self, intervals, newInterval):
        start = None
        end = None
        
        for i, (s, e) in enumerate(intervals):
            if e>=newInterval[0]:
                start = i
                break
        for i in range(len(intervals)-1, -1, -1):
            if intervals[i][0]<=newInterval[1]:
                end = i
                break
                
        if start==None:
            return intervals+[newInterval]
        elif end==None:
            return [newInterval]+intervals
        else:
            return intervals[:start] + [[min(newInterval[0], intervals[start][0]), max(newInterval[1], intervals[end][1])]] + intervals[end+1:]
            