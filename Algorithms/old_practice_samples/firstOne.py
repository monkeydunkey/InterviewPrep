'''
find index of first index in array of sorted 0s and 1s
'''

def findInd(arr):
    low = 0
    high = len(arr) - 1
    lastIndex = None
    mid = (high + low) // 2
    while high >= low:
        if arr[mid] == 1:
            if lastIndex is None or mid < lastIndex:
                lastIndex = mid
                high = mid - 1
            else:
                low = mid + 1
        else:
            low = mid + 1
        mid = (high + low) // 2
    return lastIndex


if __name__ == '__main__':
    arr = [0,0,0,1,1,1,1,1,1,1]
    print findInd(arr)

