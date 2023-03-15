#Sort, then Solve
def mergeIntervals(arr):
    
    #first sort the intervals so that it's easier to look at and iterate over
    #make new intervals for merged intervals
    #start and end variables are at the first item in intervals
    #create different start and end variables to traverse through each item 
    
    intervals = sorted(arr)
    newIntervals = []
    
    start = intervals[0]
    end = intervals [0]
    
    for s, e in intervals[1:]:
        if s > end:
            newIntervals.append((start, end))
            start = s
            end = e
        else:
            
    
    return intervals
        
print(mergeIntervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
