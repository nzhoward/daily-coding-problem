class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
def build_tree(preorder, inorder, in_start, in_end):
    if in_start > in_end:
        return None
    tmp = Node(preorder[build_tree.pre_index])
    build_tree.pre_index += 1

    if in_start == in_end:
        return tmp

    in_index = inorder.index(tmp.val)

    tmp.left = build_tree(preorder, inorder, in_start, in_index - 1)
    tmp.right = build_tree(preorder, inorder, in_index + 1, in_end)

    return tmp


def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print_inorder.ret.append(node.val)
    print_inorder(node.right)


preorder1 = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder1 = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
build_tree.pre_index = 0
built = build_tree(preorder1, inorder1, 0, len(preorder1) - 1)
print_inorder.ret = []
print_inorder(built)
print(print_inorder.ret)
