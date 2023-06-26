#Question 2: Build A Heap

import heapq

class Heap:
    def __init__(self):
        self.arr = []
    
    def top(self):
        return self.arr[0]
    
    def insert(self, x):
        heapq.heappush(self.arr, x)

    def remove(self):
        heapq.heappop(self.arr)

if __name__ == '__main__':
    myHeap = Heap()
    myHeap.insert(5)
    myHeap.insert(6)
    # myHeap.insert(7)
    # myHeap.insert(9)
    # myHeap.insert(13)
    # myHeap.insert(11)
    # myHeap.insert(10)
    
    print("this is my heap: ")
    print(myHeap) #{<__main__.Heap object at 0x7f25dd2a24d0>}
    print("----------")
    print(myHeap.top()) #{5}
    myHeap.remove()
    print(myHeap.top()) #{6}
