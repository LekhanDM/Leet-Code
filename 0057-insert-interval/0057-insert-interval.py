class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        inserted = False
        for start,end in intervals:
            if end < newInterval[0]:
                result.append([start,end])
            elif start <=newInterval[1]:
                newInterval[0]=min(newInterval[0],start)
                newInterval[1]=max(newInterval[1],end)
            else:
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append([start,end])
        if not inserted:
            result.append(newInterval)
                
        return result