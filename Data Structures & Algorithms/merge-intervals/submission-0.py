class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        for s,e in intervals[1:]:
            le = output[-1][1]
            if s<=le:
                output[-1][1] = max(e,le)
            else:
                output.append([s,e])
        return output