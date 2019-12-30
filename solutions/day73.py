class Node():
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        ret = ''
        head = self
        while head != None:
            ret += str(head.val) + '->'
            head = head.nxt
        return ret


def reverse(head):
    prev = None
    cur = head
    nxt = None
    while cur != None:
        nxt = cur.nxt
        cur.nxt = prev
        prev = cur
        cur = nxt
    return prev


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.nxt = n2
n2.nxt = n3
n3.nxt = n4

print(n1)

print(reverse(n1))
