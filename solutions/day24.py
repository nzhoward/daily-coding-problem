class Node:
    def __init__(self, val, left=None, right=None, par=None):
        self.val = val
        self.left = left
        self.right = right
        self.par = par
        self.locked = False
    
    def is_locked(self):
        return self.locked

    def are_children_locked(self):
        if self.left is not None:
            if self.left.is_locked():
                return True
            return self.left.are_children_locked()
        if self.right is not None:
            if self.right.is_locked():
                return True
            return self.right.are_children_locked()
        return False

    def are_ancestors_locked(self):
        if self.par is not None:
            cur = self.par
            while cur:
                if cur.is_locked():
                    return True
                cur = cur.par
            return False
        return False
        
    def lock(self):
        if not self.are_children_locked():
            if self.par is None or not self.par.is_locked():
                self.locked = True
                print(self.val + ' locked = ' + str(self.is_locked()))
                return True
        else:
            print(self.val + ' locked = ' + str(self.is_locked()))
            return False

    def unlock(self):
        if not self.par.is_locked() and not self.are_children_locked():
            self.locked = False
            print(self.val + ' locked = ' + str(self.is_locked()))
            return True
        else:
            print(self.val + ' locked = ' + str(self.is_locked()))
            return False


print('O(m+h) Node')
print('===========')
            
"""
    a
   / \
  b   c
 / \
d   e

"""

a = Node('a', None, None, None)
b = Node('b', None, None, a)
c = Node('c', None, None, a)

a.left = b
a.right = c

d = Node('d', None, None, b)
e = Node('e', None, None, b)

b.left = d
b.right = e

b.lock()
c.lock()
a.lock()
b.unlock()


class EfficientNode:
    def __init__(self, val, left=None, right=None, par=None):
        self.val = val
        self.left = left
        self.right = right
        self.par = par
        self.locked = False
        self.locked_children_count = 0

    def is_locked(self):
        return self.locked

    def can_lock_or_unlock(self):
        if self.locked_children_count > 0:
            return False

        cur = self.par
        while cur:
            if cur.is_locked():
                return False
            cur = cur.par

        return True

    def lock(self):
        if self.can_lock_or_unlock():
            self.locked = True

            cur = self.par
            while cur:
                cur.locked_children_count += 1
                cur = cur.par
            print(self.val + ' locked = ' + str(self.is_locked()))
            return True
        else:
            print(self.val + ' locked = ' + str(self.is_locked()))
            return False

    def unlock(self):
        if self.can_lock_or_unlock():
            self.locked = False

            cur = self.par
            while cur:
                cur.locked_children_count -= 1
                cur = cur.par
            print(self.val + ' locked = ' + str(self.is_locked()))
            return True
        else:
            print(self.val + ' locked = ' + str(self.is_locked()))
            return False

        
print('')
print('O(h) Node')
print('=========')

"""
    a
   / \
  b   c
 / \
d   e

"""

a = EfficientNode('a', None, None, None)
b = EfficientNode('b', None, None, a)
c = EfficientNode('c', None, None, a)

a.left = b
a.right = c

d = EfficientNode('d', None, None, b)
e = EfficientNode('e', None, None, b)

b.left = d
b.right = e

b.lock()
c.lock()
a.lock()
b.unlock()
