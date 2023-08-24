import heapq

class runningMedian:
    def __init__(self):
        self.min_heap = []  # To store larger half of numbers
        self.max_heap = []  # To store smaller half of numbers

    def addNum(self, num: int) -> None:
        # Put negative of num in max heap to simulate a min heap
        heapq.heappush(self.max_heap, -num)

        # Pop the maximum element from max heap and push it into min heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # If the sizes of heaps are unequal, rebalance them
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            # If the total number of elements is even, take the average of middle elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            # Otherwise, the median is the middle element in max heap
            return -self.max_heap[0]
