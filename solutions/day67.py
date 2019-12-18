import heapq

class Node():
    def __init__(self, key, val, tick):
        self.key = key
        self.val = val
        self.freq = 0
        self.tick = tick

    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        elif self.freq == other.freq:
            return self.tick < other.tick
        return False

    def __gt__(self, other):
        if self.freq > other.freq:
            return True
        elif self.freq == other.freq:
            return self.tick > other.tick
        return False

    def __repr__(self):
        return str(self.val)
    

class MyHeap():
    def __init__(self):
        self.hq = list()
        heapq.heapify(self.hq)
        self.size = 0

    def __str__(self):
        ret = ''
        for i in self.hq:
            ret += '(' + str(i.key) + ':' + str(i.freq) + ':' + str(i.tick) + ')' + '->'
        return ret
    
    def push(self, node):
        heapq.heappush(self.hq, node)
        self.size = len(self.hq)

    def pop(self):
        ret = heapq.heappop(self.hq)
        self.size = len(self.hq)
        return ret


class LFUCache():
    def __init__(self, size):
        self.heap = MyHeap()
        self.cache = dict()
        self.size = size
        self.tick = 0

    def set_val(self, key, value):
        self.tick += 1
        if key not in self.cache:
            if self.heap.size == self.size:
                # Remove least frequent
                key_to_del = self.heap.pop().key
                self.cache.pop(key_to_del)

            # Store new value in cache
            new = Node(key, value, self.tick)
            
            self.cache[key] = new
            self.heap.push(new)
        else:
            self.touch(key)

    def get_val(self, key):
        if key not in self.cache:
            return -1
        self.tick += 1
        self.touch(key)
        return self.cache[key].val

    def touch(self, key):
        tmp = self.cache[key]
        tmp.freq += 1
        tmp.tick = self.tick
        heapq.heapify(self.heap.hq)


cache = LFUCache(4)

print('Build initial values')
cache.set_val(1, 4)
cache.set_val(2, 2)
cache.set_val(3, 5)
cache.set_val(4, 3)

print(cache.heap)
print(cache.cache)
print('')

print('Access values to increase counts')
cache.get_val(1)
cache.get_val(1)
cache.get_val(1)

cache.get_val(2)
cache.get_val(2)

cache.get_val(3)

cache.get_val(4)
cache.get_val(4)
cache.get_val(4)
cache.get_val(4)

print(cache.heap)
print(cache.cache)
print('')

print('Set new key to pop least frequently used')
cache.set_val(5, 10)

print(cache.heap)
print(cache.cache)
print('')

print('Set new key to pop least frequently used')
cache.set_val(6, 10)

print(cache.heap)
print(cache.cache)
print('')

print('Set new key to pop least frequently used')
cache.get_val(6)
cache.get_val(6)
cache.get_val(6)
cache.get_val(6)
cache.get_val(6)

cache.set_val(7, 12)

print(cache.heap)
print(cache.cache)
print('')

print('Increase freq to test ordering of same freqs by looking at ticks')
cache.get_val(7)
cache.get_val(7)
cache.get_val(7)

print(cache.heap)
print(cache.cache)
print('')

print('Increase freq to test removing least recently used for same freqs')
cache.set_val(8, 9)

print(cache.heap)
print(cache.cache)
print('')
