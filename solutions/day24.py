class Node:
    def __init__(self, val, left=None, right=None, par=None):
        self.val = val
        self.left = left
        self.right = right
        self.par = par
        self.locked = False
    
    def is_locked(self):
        return self.locked

    def is_children_locked(self):
        ret = False
        print(self.val + str(self.locked))
        if self.locked:
            return True
        if self.left is not None:
            ret = self.left.is_children_locked()
        if self.right is not None:
            ret = self.right.is_children_locked()
        return ret
            
    
a = Node('a', None, None, None)
b = Node('b', None, None, a)
c = Node('c', None, None, a)

a.left = b
a.right = c
#c.locked = True

d = Node('d', None, None, b)
e = Node('e', None, None, b)

b.left = d
b.right = e
e.locked = True

print(a.is_children_locked())
