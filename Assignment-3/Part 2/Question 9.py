import heapq

def mergeKSortedArrays(k, arr):
    heap = []
    res = []
    for i in range(k):
        if arr[i]:
            heap.append((arr[i][0], i, 0))
    heapq.heapify(heap)
    while heap:
        val, arrIndex, index = heapq.heappop(heap)
        res.append(val)
        if index + 1 < len(arr[arrIndex]):
            heapq.heappush(heap, (arr[arrIndex][index + 1], arrIndex, index+1))
    return res

print(mergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
#output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
print(mergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
#output: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
