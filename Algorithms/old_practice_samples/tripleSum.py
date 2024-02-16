'''
Given N distinct integers, how many triples sum to exactly 0
Simple count:
RunTime - n^3
Space Complexity - n

Increasing Sets
RunTime - n^3
Space Complexity - n^2

So even though the second solution seems more elegant it is actually much worse

Sort and Search
RunTime: nlogn + n^2*logn = worst case n^2 * logn
Space Complexity - n
'''

def simpleCount(arr):
    count = 0
    for i, a1 in enumerate(arr):
        print arr[i+1:]
        for j, a2 in enumerate(arr[i+1:]):
            j += i+1
            for k, a3 in enumerate(arr[j+1:]):
                if a1 + a2 + a3 == 0:
                    print a1, a2, a3
                    count += 1

    return count

def binarySearch(arr, a):
    hi = len(arr) - 1
    lo = 0 
    while lo <= hi:
        mid = (hi + lo)/2
        if arr[mid] == a:
            return mid
        elif arr[mid] < a:
            lo = mid + 1
        else:
            hi = mid - 1
    return None

def sortAndSearch(arr):
    '''
    First sort the arr and then for each combo search for the remaining value for sum to be 0
    '''
    arr = sorted(arr)
    count = 0
    for i in xrange(len(arr)):
        for j in xrange(i+1, len(arr)):
            toSearch = 0 - (arr[i] + arr[j])
            ind = binarySearch(arr, toSearch)
            if ind is not None and ind > j:
                count += 1
    return count

def increasingSets(arr):
    finalarr = []
    posCount = []
    count = 0
    for a in arr:
        temp = []
        tempCount = []
        for i, en in enumerate(finalarr):
            temp.append(en+a)
            tempCount.append(posCount[i] + 1)
            if tempCount[-1] >=3:
                count += 1 if temp[-1] == 0 else 0
                temp.pop()
                tempCount.pop()
        finalarr.extend(temp)
        posCount.extend(tempCount)
        finalarr.append(a)
        posCount.append(1)
    return count

def test_simpleCount():
    arr = [30, -40, -20, -10, 40, 0, 10, 5]
    assert simpleCount(arr) == 4

def test_increasingSets():
    arr = [30, -40, -20, -10, 40, 0, 10, 5]
    assert increasingSets(arr) == 4

def test_sortAndSearch():
    arr = [30, -40, -20, -10, 40, 0, 10, 5]
    assert sortAndSearch(arr) == 4
