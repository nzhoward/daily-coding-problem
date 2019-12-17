import heapq

class MyHeap():
    def __init__(self, size):
        self.hq = []
        heapq.heapify(self.hq)
        self.size = size

    def __str__(self):
        return str(self.hq)
    
    def push(self, ele):
        heapq.heappush(self.hq, ele)

    def pop(self):
        heapq.heappop(self.hq)


class LFUCache():
    def __init__(self, size):
        self.heap = None
        self.cache = {}
        self.size = size

    def set_val(self, key, value):
        if key not in self.cache:
            if self.heap is None:
                self.heap = MyHeap(self.size)
                self.cache[key] = value


heap = MyHeap(5)
heap.push(4)
heap.push(2)
heap.push(5)
heap.push(3)
print(heap)
