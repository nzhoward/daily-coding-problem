class Node():
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = None

    def __str__(self):
        return str(self.val)
    

class MyStack():
    def __init__(self):
        self.head = None

    def __str__(self):
        tmp = self.head
        ret = ''
        while tmp is not None:
            ret += str(tmp) + '->'
            tmp = tmp.nxt
        return ret

    def push(self, other):
        other.nxt = self.head
        self.head = other

    def pop(self):
        if self.head is not None:
            ret = self.head
            self.head = self.head.nxt
        return ret


class MyQueue():
    def __init__(self):
        self.left = MyStack()
        self.right = MyStack()
    
    def enqueue(self, other):
        self.left.push(other)
        print('enqueued:', other)

    def dequeue(self):
        if self.right.head is None:
            while self.left.head is not None:
                self.right.push(self.left.pop())
        print('dequeued:', self.right.head)
        return self.right.pop()


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

stack = MyStack()
stack.push(node1)
stack.push(node2)
stack.push(node3)
print(stack)
print(stack.pop())
print(stack)

print('------')

queue = MyQueue()
queue.enqueue(node1)
queue.enqueue(node2)
queue.dequeue()
queue.enqueue(node3)
queue.dequeue()
queue.enqueue(node4)
queue.dequeue()
queue.dequeue()
