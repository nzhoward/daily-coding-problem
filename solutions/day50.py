class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def evaluate(root):
    if root.val == '+':
        return evaluate(root.left) + evaluate(root.right)
    elif root.val == '-':
        return evaluate(root.left) - evaluate(root.right)
    elif root.val == '*':
        return evaluate(root.left) * evaluate(root.right)
    elif root.val == '/':
        return evaluate(root.left) / evaluate(root.right)
    else:
        return root.val

'''
    *
   / \
  +    +
 / \  / \
3  2  4  5
'''

n3 = Node(3)
n2 = Node(2)
n4 = Node(4)
n5 = Node(5)
nplus1 = Node('+', n3, n2)
nplus2 = Node('+', n4, n5)
nstar = Node('*', nplus1, nplus2)

print(evaluate(nstar))
