class Node():
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

    def __str__(self):
        ret = ''
        tmp = self
        while tmp is not None:
            ret += str(tmp.val) + '->'
            tmp = tmp.nxt
        return ret

    def get_size(self):
        ret = 1
        tmp = self
        while tmp is not None:
            ret += 1
            tmp = tmp.nxt
        return ret

    def get_2nd_last(self):
        tmp = self
        while tmp.nxt.nxt is not None:
            tmp = tmp.nxt
        return tmp


class LRUCache():
    def __init__(self, size):
        self.queue = None
        self.cache = {}
        self.size = size

    def set_val(self, key, value):
        if key not in self.cache:
            if self.queue is None:
                new = Node(key)
                self.queue = new
                self.cache[key] = new
            elif self.queue.get_size() <= self.size:
                new = Node(key)
                new.nxt = self.queue
                self.queue.prev = new
                self.queue = new
                self.cache[key] = new
            else:
                new = Node(key)
                new.nxt = self.queue
                self.queue.prev = new
                tmp = self.queue.get_2nd_last()
                self.cache.pop(tmp.nxt.val)
                tmp.nxt = None
                self.queue = new
                self.cache[key] = new
        else:
            tmp = self.cache[key]
            if tmp.prev is not None:
                tmp.prev.nxt = tmp.nxt
            if tmp.nxt is not None:
                tmp.nxt.prev = tmp.prev
            tmp.nxt = self.queue
            self.queue.prev = tmp
            self.queue = tmp

    def get_val(self, key):
        tmp = self.cache[key]
        if tmp.prev is not None:
            tmp.prev.nxt = tmp.nxt
        if tmp.nxt is not None:
            tmp.nxt.prev = tmp.prev
        tmp.nxt = self.queue
        self.queue.prev = tmp
        self.queue = tmp

        return self.queue.val


cache = LRUCache(3)
cache.set_val(1, 1)
cache.set_val(2, 2)
cache.set_val(3, 3)
print(cache.queue)
cache.set_val(4, 4)
print(cache.queue)
cache.set_val(2, 2)
print(cache.queue)
cache.get_val(3)
print(cache.queue)
cache.get_val(2)
print(cache.queue)
cache.get_val(4)
print(cache.queue)
