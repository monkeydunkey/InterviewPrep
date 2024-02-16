'''
Given a set of pts with a list of connection between 2 pts. Answer if 2 points are transitively 
connected or not

Answer:
We can use sets to maintain the set of connected vertices.
1. One of the vertex is part of a set add the other to that set
2. if both are part of some set merge the 2 sets together
3. If neithere are part of any of the existing set create a new set to store them

Runtime (Worst Case)
Initialization   Union    Find
      1            N       N
'''
import pytest

def union(tup, setList):
    s1, s2 = None, None
    s1I, s2I = None, None
    for i, s in enumerate(setList):
        if tup[0] in s:
            s1 = s
            s1I = i
        if tup[1] in s:
            s2 = s
            s2I = i
    if s1 is None and s2 is None:
        setList.append(set(tup))
    elif s2 is None:
        s1.add(tup[1])
    elif s1 is None:
        s2.add(tup[0])
    else:
        s1 = s1.union(s2)
        setList[s1I] = s1
        setList.pop(s2I)

def checkConnectivity(tup, setList):
    print setList
    i1, i2 = None, None
    for i, s in enumerate(setList):
        if tup[0] in s:
            i1 = i
        if tup[1] in s:
            i2 = i
    return i1 == i2

def test_unionLogic():
    setList = []
    union((0,1), setList)
    union((0,2), setList)
    union((3,4), setList)
    union((2,3), setList)
    assert checkConnectivity((2,3), setList) == True
    assert checkConnectivity((1,4), setList) == True

def test_checkNegative():
    setList = []
    union((0,1), setList)
    union((2,3), setList)
    assert checkConnectivity((1,3), setList) == False

def test_checkSimple():
    setList = []
    union((0,1), setList)
    assert checkConnectivity((1,0), setList) == True

