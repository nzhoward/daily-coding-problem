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


def merge_lists_O_N(lists):
    finished = False
    ret = Node(None)
    head = ret
    while not finished:
        min_val = float('+inf')
        min_idx = 0
        
        for i in range(len(lists)):
            if lists[i] is None:
                continue
            if lists[i].val < min_val:
                min_val = lists[i].val
                min_idx = i
        
        lists[min_idx] = lists[min_idx].nxt
        head.nxt = Node(min_val)
        head = head.nxt
        
        if not all_none(lists):
            continue
        finished = True

    return ret.nxt


def all_none(lists):
    for l in lists:
        if l is not None:
            return False
    return True
    


l1 = Node(1)
l1.nxt = Node(2)
l1.nxt.nxt = Node(4)

l2 = Node(3)
l2.nxt = Node(4)
l2.nxt.nxt = Node(5)

l3 = Node(2)
l3.nxt = Node(3)
l3.nxt.nxt = Node(6)

print(merge_lists_O_N([l1, l2, l3]))
