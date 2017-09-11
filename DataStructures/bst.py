'''
Binary Search Tree implementation
'''

class binaryNode(object):
    def __init__ (self, key, value, parent):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
        self.parent = parent


class binarySearchTree:
    
    def __init__ (self):
        self.head = None

    def add (self, key, value):
        if self.head is None:
            self.head = binaryNode(key, value, None)
        else:
            temp = self.head
            prev = self.head
            while temp is not None:
                prev = temp
                if temp.key > key:
                    temp = temp.left
                else:
                    temp = temp.right
            if prev.key > key:
                prev.left = binaryNode(key, value, prev)
            else:
                prev.right = binaryNode(key, value, prev)
    
    # search the value of a node with the given key value
    def search(self, key):
        temp = self.head
        ret = None
        while temp is not None:
            if temp.key == key:
                ret = temp
                break
            elif temp.key > key:
                temp = temp.left
            else:
                temp = temp.right
        return ret

    def update(self, key, value):
        node = self.search(key)
        if node is None:
            return False
        else:
            node.value = value
            return True
    
    def findSucessor(self, key):
        node = self.search(key)
        if node is None:
            return None
        
        #Now to find the smallest biggest number
        tempNode = node.right
        succ = node
        while tempNode is not None:
            succ = tempNode
            tempNode = tempNode.left
        return succ
    '''
    There are a lot of cases that still needs handling, espcially how to delete succ node 
    as its parent ref needs to be updated
    '''
    def delete(self,key):
        #there are 3 cases which needs to handled
        node = self.search(key)
        if node is None:
            return "The key does not exixts"
        succ = self.findSucessor(node.key)
        if succ == node:
            if node.left is not None:
                node.key, node.left.key = node.left.key, node.key
                node.value, node.left.value = node.left.value, node.value
                node.left = None
            else:
                if node == self.head:
                    self.head = None
                else:
                    if node.parent.left == node:
                        node.parent.left = None
                    else:
                        node.parent.right = None
        else:
            node.value, succ.value = succ.value, node.value
            node.key, succ.key = succ.key, node.key
            if succ.right is not None:
                if succ.parent.right == succ:
                    succ.parent.right = succ.right
                else:
                    succ.parent.left = succ.left
            else:
                if succ.parent.right == succ:
                    succ.parent.right = None
                else:
                    succ.parent.left = None
        






