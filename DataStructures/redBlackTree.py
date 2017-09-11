'''
Red Black Tree Implementation with the following functionality
1. Insert
2. Search 
3. delete
4. inroder traversal
'''

class treeNode:
    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        #0 rep black color and 1 red
        self.color = 0

class redBlackTree():
    def __init__(self):
        self.head = None
    
    def rotate(self, node, l):
        rep = node.right if l == 1 else node.left
        par = node.parent
        if par is None:
            self.head = rep

        elif par.left == node:
            par.left = rep
        else:
            par.right = rep
        rep.parent = par
        if l == 1:
            node.right = rep.left
            rep.left = node
        else:
            node.left = rep.right
            rep.right = node
        node.parent = rep
        if not node.color:
            node.color = 1
            rep.color = 0


    def rotateLeft(self, node):
        rep = node.right
        node.right = rep.left
        par = node.parent
        if par.left == node:
            par.left = rep
        else:
            par.right = rep
        rep.parent = par
        rep.left = node
        node.parent = rep
        #taking care of color change
        if not node.color:
            rep.color = 0
            node.color = 1

    def rotateRight(self, node):
        rep = node.left
        node.left = rep.right
        par = node.parent
        if par.left == node:
            par.left = rep
        else:
            par.right = rep
        rep.parent = par
        rep.right = node
        node.parent = rep
        if not node.color:
            rep.color = 0
            node.color = 1

    
    def recurseUpdate(self, parent, child):
        print ((child.color != parent.color) and parent.left == child) 
        if ((child.color != parent.color) and parent.left == child) or (parent.color == 0 and child.color== 0):
            return
        if parent.right == child and parent.left is None:
            self.rotate(parent, 1)
        print parent.key, child.key, parent.color, child.color
        if parent.color == 1 and child.color == 1:
            toMove = parent if parent.parent != child else child
            toMove = toMove.parent
            self.rotate(toMove, 0)
        toCheck = parent if parent.parent != child else child
        if toCheck.left is not None and toCheck.right is not None and toCheck.left.color and toCheck.right.color:
            toCheck.left.color, toCheck.right.color = 0, 0
            if toCheck == self.head:
                toCheck.color = 0
            else:
                toCheck.color = 1
                self.recurseUpdate(toCheck.parent, toCheck)

 

    def add(self, key, value):
        if self.head is None:
            self.head = treeNode(key, value, None)
        else:
            temp = self.head
            prev = self.head
            while temp is not None:
                prev = temp
                if temp.key > key:
                    temp = temp.left
                else:
                    temp = temp.right
                node = treeNode(key, value, prev)
                node.color = 1
            if prev.key > key:
                prev.left = node
            else:
                prev.right = node

                #Need to update and handle the inconc
            self.recurseUpdate(prev, node)

if __name__ == '__main__':
    rbt = redBlackTree()
    rbt.add(1,1)
    rbt.add(2,1)
    rbt.add(0,1)
    print rbt.head.key, rbt.head.color, rbt.head.right.key, rbt.head.right.color, rbt.head.left.key, rbt.head.left.color
