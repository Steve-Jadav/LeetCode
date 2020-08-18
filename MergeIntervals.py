# Problem 56

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == None or len(intervals) == 0:
            return []
        
        intervals.sort(key = lambda x: x[0])
        result = list()
        
        first = intervals[0]
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] <= first[1]:
                first[1] = max(first[1], current[1])
            else:
                result.append(first)
                first = current
            
        result.append(first)
        return result
