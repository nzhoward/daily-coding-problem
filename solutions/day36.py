class Node:
    def __init__(self, val, left=None, right=None, par=None):
        self.val = val
        self.left = left
        self.right = right
        self.par = par


def find_second_largest_in_bst(root):
    cur = root
    while cur.right is not None:
        cur = cur.right
    if cur.left is None and cur.right is None:
        return cur.par.val
    elif cur.left is not None and cur.right is None:
        return cur.left.val
    elif cur.left is None and cur.right is not None:
        return cur
    

one = Node(1)
six = Node(6)
fourteen = Node(14)

three = Node(3, one, six)
ten = Node(10, None, fourteen)

eight = Node(8, three, ten)

three.par = eight
one.par = three
six.par = three

ten.par = eight
fourteen.par = ten

thirteen = Node(13, None, None, fourteen)
fourteen.left = thirteen

print(find_second_largest_in_bst(eight))
