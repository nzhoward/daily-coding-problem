class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(in_node):
    def do_serialize(the_node, tree_string):
        if the_node is None:
            tree_string += 'None,'
        else:
            tree_string += str(the_node.val) + ','
            tree_string = do_serialize(the_node.left, tree_string)
            tree_string = do_serialize(the_node.right, tree_string)
        return tree_string

    ret = do_serialize(in_node, '')
    print(ret)
    return ret


def deserialize(tree_string):
    def do_deserialize(node_list):
        if node_list[0] == 'None':
            node_list.pop(0)
            return None
        root = Node(node_list[0])
        node_list.pop(0)
        root.left = do_deserialize(node_list)
        root.right = do_deserialize(node_list)
        return root

    return do_deserialize(tree_string.split(','))
        

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
