#Sort, then Solve
def mergeIntervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    
    return merged
    
print(mergeIntervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)])) #Output: [(4, 8), (1, 3), (9, 12)]
print(mergeIntervals([(5, 8), (6, 10), (2, 4), (3, 6)]) #Output: [(2, 10)]
print(mergeIntervals([(10, 12), (5, 6), (7, 9), (1, 3)]) #Output: [(10, 12), (5, 6), (7, 9), (1, 3)]
