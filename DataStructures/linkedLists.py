class node(object):
    def __init__(self, val, nextNode, prevNode=None):
        self.val = val
        self.nextNode = nextNode
        self.prevNode = prevNode

class linkedList(object):
    def __init__(self):
        self.head = None
    
    def add(self, val):
        if self.head is None:
            self.head = node(val, None)
        else:
            prevHead = self.head
            while prevHead.nextNode is not None:
                prevHead = prevHead.nextNode
            prevHead.nextNode = node(val, None)
    
    def remove(self, lifo):
        if self.head is None:
            return 'The list is empty'
        else:
            retVal = None
            # Flag for last in first out
            if lifo:
                runnerHead = self.head
                prevRunner = self.head
                while runnerHead.nextNode is not None:
                    prevRunner = runnerHead
                    runnerHead = runnerHead.nextNode
                retVal = runnerHead.val
                prevRunner.nextNode = None
                del runnerHead
            else:
                tempNode = self.head
                self.head = self.head.nextNode
                retVal = tempNode.val
                del tempNode
            return retVal

    def getList(self):
        retList = []
        runnerHead = self.head
        while runnerHead is not None:
            retList.append(runnerHead.val)
            runnerHead = runnerHead.nextNode
        return retList

    def top(self):
        return 'NA' if self.head is None else self.head.val

if __name__ == '__main__':
    ll = linkedList()
    for x in xrange(12):
        ll.add(x)
    print ll.getList()
    ll.remove(True)
    print ll.getList()
    ll.remove(False)
    print ll.top()





