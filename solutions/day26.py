class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        ret = ''
        cur = self
        while cur.nxt:
            ret += cur.val + '->'
            cur = cur.nxt
        return ret
    
    def remove_kth_last_naive(self, k):
        length = 0
        cur = self
        while cur.nxt:
            length += 1
            cur = cur.nxt
        tmp = length - k - 1
        cur = self
        for i in range(tmp):
            cur = cur.nxt
        cur.nxt = cur.nxt.nxt

    def remove_kth_one_pass_dict(self, k):
        dic = {}
        length = 0
        cur = self
        while cur.nxt:
            dic[length] = cur
            length += 1
            cur = cur.nxt
        tmp = length - k - 1
        dic[tmp].nxt = dic[tmp + 1].nxt

    def remove_kth_two_pointers(self, k):
        head = self
        tail = self
        for i in range(k + 1):
            head = head.nxt
        while head.nxt:
            head = head.nxt
            tail = tail.nxt
        tail.nxt =  tail.nxt.nxt
        
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

print('Naive:')
a.nxt = b
b.nxt = c
c.nxt = d
d.nxt = e
e.nxt = f

print(a)
a.remove_kth_last_naive(3)
print(a)
a.remove_kth_last_naive(1)
print(a)

print('')
print('One Pass Dict:')
a.nxt = b
b.nxt = c
c.nxt = d
d.nxt = e
e.nxt = f

print(a)
a.remove_kth_one_pass_dict(3)
print(a)
a.remove_kth_one_pass_dict(1)
print(a)

print('')
print('One Pass Two Pointers:')
a.nxt = b
b.nxt = c
c.nxt = d
d.nxt = e
e.nxt = f

print(a)
a.remove_kth_two_pointers(3)
print(a)
a.remove_kth_two_pointers(1)
print(a)
