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
        if self.locked:
            return True
        self.left.is_children_locked()
        self.right.is_children_locked()
        return False


a = Node(1, None, None, None)
b = Node(2, None, None, a)
c = Node(3, None, None, a)
a.left = b
a.right = c
#c.locked = True
print(a.locked)        
print(a.left)
print(a.right)
print(a.is_children_locked())
