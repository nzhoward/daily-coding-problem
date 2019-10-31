class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        ret = ''
        cur = self
        while cur is not None:
            ret += str(cur.val) + ' -> '
            cur = cur.nxt
        return ret


def find_intersection(node_1, node_2):
    cur = node_1
    nodes = set()
    while cur is not None:
        nodes.add(cur)
        cur = cur.nxt
    cur = node_2
    while cur is not None:
        if cur in nodes:
            return cur
        cur = cur.nxt
        

a = Node(3)
b = Node(7)
c = Node(8)
d = Node(10)

a.nxt = b
b.nxt = c
c.nxt = d

e = Node(99)
f = Node(1)

e.nxt = f
f.nxt = c

print(a)
print(e)

intersection = find_intersection(a, e)
print(intersection.val)
