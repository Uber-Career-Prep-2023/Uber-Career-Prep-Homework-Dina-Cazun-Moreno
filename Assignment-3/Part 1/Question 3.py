#Build a Priority Queue

import heapq

class PriorityQueue:
    def __init__(self):
        self.arr = []
    
    def top(self):
        return self.arr[0][1]
    
    def insert(self, x, weight):
        heapq.heappush(self.arr, (weight, x))

    def remove(self):
        heapq.heappop(self.arr)

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert(5, 1)
    pq.insert(6, 2)
    
    print("this is my priority queue: ")
    print(pq) #{<__main__.PriorityQueue object at 0x7f4b4f1a2590>}
    print("----------")
    print(pq.top()) #{5}
    pq.remove()
    print(pq.top()) #{6}
