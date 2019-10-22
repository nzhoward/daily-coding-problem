class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival(node):
    global cnt
    if node is None:
        return
    elif node.left is None and node.right is None:
        cnt += 1
    elif node.left is None or node.right is None:
        return
    elif node.left.val == node.right.val:
        cnt += 1
    if node.left is not None:
        count_unival(node.left)
    if node.right is not None:
        count_unival(node.right)
    return cnt


def print_tree(node):
    print(node.val, end=' ')
    if node.left is not None:
        print_tree(node.left)
    if node.right is not None:
        print_tree(node.right)


"""
  0
 / \
1   0
   / \
  1   0
 / \
1   1
"""
cnt = 0

root = Node(0)
one1 = Node(1)
one2 = Node(0)
root.left = one1
root.right = one2

two1 = Node(1)
two2 = Node(0)
one2.left = two1
one2.right = two2

three1 = Node(1)
three2 = Node(1)
two1.left = three1
two1.right = three2

print_tree(root)
print('')
print(count_unival(root))


"""
  1
 / \
1   1
   / \
  1   1
 / \
1   1
"""
cnt = 0

root = Node(1)
one1 = Node(1)
one2 = Node(1)
root.left = one1
root.right = one2

two1 = Node(1)
two2 = Node(1)
one2.left = two1
one2.right = two2

three1 = Node(1)
three2 = Node(1)
two1.left = three1
two1.right = three2

print_tree(root)
print('')
print(count_unival(root))
