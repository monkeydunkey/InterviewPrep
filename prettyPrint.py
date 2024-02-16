def prettyPrint(A):
    recWidth = 2*A - 1
    val = range(A, 0, -1)
    mid = A
    ptStr = [' '.join(list(str(A)*recWidth))]
    for i in xrange(mid - 1):
        newStrs = ptStr[-1].split(' ')
        newStrs[i+1: i+1 + 2*val[i+1]-1] =  [str(val[i+1])]*(2*val[i+1] - 1)
        ptStr.append(' '.join(newStrs))
    for re in ptStr:
        print re
    for re in reversed(ptStr[:-1]):
        print re

prettyPrint(4)
