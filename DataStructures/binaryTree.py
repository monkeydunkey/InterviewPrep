#Binary Tree implementation

class treeNode(object):
    def __init__(self, val):
        self.key = val
        self.right = None
        self.left = None


class binaryTree(object):
    def __init__(self, val):
        self.root = treeNode(val)

    def findKeyAdd(self, node):
        if node is None:
            return None
        else:
            if node.left is None or node.right is None:
                return node
            else:
                leftSearch = self.findKeyAdd(node.left)
                return leftSearch if leftSearch is not None else self.findKeyAdd(node.right)

    def add(self, val):
        parNode = self.findKeyAdd(self.root)
        if parNode.left is None:
            parNode.left = treeNode(val)
        else:
            parNode.right = treeNode(val)

    def recurTrav(self, node):
        if node is None:
            return 
        else:
            self.recurTrav(node.left)
            print node.key
            self.recurTrav(node.right)

    def inOrderTraversal(self):
        self.recurTrav(self.root)


if __name__ == '__main__':
    bt = binaryTree(1)
    for x in xrange(2, 8):
        bt.add(x)
    bt.inOrderTraversal()

