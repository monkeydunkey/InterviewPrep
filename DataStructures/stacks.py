#We will be using the in-built list for the purpose initially
class stack(object):
    def __init__(self):
        self.li = []

    def push(self, val):
        self.li.append(val)

    def pop(self):
        if len(self.li) == 0:
            return 'The Stack is empty'
        ret = self.li[-1]
        del self.li[-1]
        return ret
    
    def peek(self):
        return 'Stack is empty' if len(self.li) == 0 else self.li[0]

from linkedLists import linkedList
class stackLinkedList(object):
    def __init__(self):
        self.li = linkedList()

    def push(self, val):
        self.li.add(val)

    def pop(self):
        return self.li.remove(True)

    def peek(self):
        return self.li.top()

if __name__ == '__main__':
    st = stackLinkedList()
    st.push(12)
    st.push(13)
    print st.pop()
    print st.pop()
    print st.pop()
    print st.peek()
    for x in xrange(12):
        st.push(x)
    print st.li
