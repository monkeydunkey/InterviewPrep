'''
A gene is represented as a string of length n (where n is divisible by 4), composed of the letters A, G,T, C, and . It is considered to be steady if each of the four letters occurs exactly  times. For example,  and  are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string . It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of  and replace it with any string of the same length.

Modifying a large substring of bear genes can be dangerous. Given a string , can you help Limak find the length of the smallest possible substring that he can replace to make  a steady gene?

Note: A substring of a string  is a subsequence made up of zero or more consecutive characters of .
'''

def checkSolution(st,start, end, maxPerChar):
    lCountDict = {}
    rCountDict = {}
    for x in st[:start]:
        lCountDict[x] = lCountDict.get(x, 0) + 1
    for x in st[end+1:]:
        rCountDict[x] = rCountDict.get(x, 0) + 1
    return [len(filter(lambda x: lCountDict[x] > maxPerChar, lCountDict.keys())) == 0, 
            len(filter(lambda x: rCountDict[x] > maxPerChar, rCountDict.keys())) == 0]

l = 40
st = 'TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC'
maxPerChar = l/4
minTillNow = len(st)
minJ = 0
maxI = len(st)
i = 0
#arr = [[-1 for x in xrange(len(st))] for y in xrange(len(st))]
while i < maxI:
    for j in xrange(len(st)-1, minJ+i-1, -1):
        leftSatisfied, rightSatisfied = checkSolution(st, i, j, maxPerChar)
        if leftSatisfied and rightSatisfied:
            minTillNow = min(j - i +1, minTillNow)
        else:
            if not leftSatisfied:
                maxI = min(i, maxI)  
            if not rightSatisfied:
                minJ = max(j, minJ)
    i += 1
print minTillNow, minJ, maxI
print checkSolution(st, 0, 7, 4)
