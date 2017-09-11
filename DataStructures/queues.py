class queue(object):
    def __init__(self):
        self.li = []

    def enqueue(self, val):
        self.li.append(val)

    def dequeue(self):
        if len(self.li) == 0:
            return 'The queue is empty'
        else:
            retVal = self.li[0]
            del self.li[0]
            return retVal
    def peek(self):
        return 'Queue is empty' if len(self.li) == 0 else self.li[0]

if __name__ == '__main__':
    que = queue()
    que.enqueue(12)
    que.enqueue(13)
    print que.dequeue()
    print que.dequeue()
    print que.peek()
    for x in xrange(12):
        que.enqueue(x)
    print que.li
