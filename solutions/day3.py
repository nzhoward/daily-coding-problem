class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    def doSerialize(node, treeString):
        if node is None:
            treeString += 'None,'
        else:
            treeString += str(node.val) + ','
            treeString = doSerialize(node.left, treeString)
            treeString = doSerialize(node.right, treeString)
        return treeString

    ret = doSerialize(node, '')
    print(ret)
    return ret


def deserialize(treeString):
    def doDeserialize(nodeList):
        if nodeList[0] == 'None':
            nodeList.pop(0)
            return None
        root = Node(nodeList[0])
        nodeList.pop(0)
        root.left = doDeserialize(nodeList)
        root.right = doDeserialize(nodeList)
        return root

    return doDeserialize(treeString.split(','))
        

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
