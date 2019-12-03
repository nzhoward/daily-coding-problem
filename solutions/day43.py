class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class MaxStack():
    def __init__(self):
        self.top = None
        self.maximum = None

    def __str__(self):
        tmp = self.top
        ret = ''
        while tmp is not None:
            ret += str(tmp) + '->'
            tmp = tmp.next
        ret += '|max=' + str(self.maximum)
        return ret

    def get_max(self):
        return self.maximum
    
    def push(self, value):
        print('push:', value)
        if self.top is None:
            self.top = Node(value)
            self.maximum = value
        elif value < self.maximum:
            tmp = Node(value)
            tmp.next = self.top
            self.top = tmp
        else:
            tmp = Node(2 * value - self.maximum)
            self.maximum = value
            tmp.next = self.top
            self.top = tmp

    def pop(self):
        if self.top is None:
            return None
        elif self.top.value < self.maximum:
            ret = self.top
            self.top = self.top.next
            return ret
        else:
            ret = self.maximum
            self.maximum = 2 * self.maximum - self.top.value
            self.top = self.top.next
            return ret
            

my_stack = MaxStack()
my_stack.push(4)
my_stack.push(2)
my_stack.push(1)
print(my_stack)
print('pop:', my_stack.pop())
print(my_stack)
my_stack.push(6)
print(my_stack)
print('pop:', my_stack.pop())
print(my_stack)
print('pop:', my_stack.pop())
print(my_stack)
