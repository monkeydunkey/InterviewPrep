def getMedian(arr):
    arrLen = len(arr)
    return arr[arrLen/2] if arrLen%2 == 1 else float(arr[arrLen/2] + arr[(arrLen/2) + 1]) / 2

def activityNotifications(expenditure, d):
    # Complete this function
    sortedArr = sorted(expenditure[:d])
    count = 0
    for day in xrange(d, len(expenditure)):
        if expenditure[day] >= 2 * getMedian(sortedArr):
            count += 1
        toRemove, toAdd = None, d-1
        for i, ele in enumerate(sortedArr):
            if expenditure[day - d] == ele:
                toRemove = i
            if ele > expenditure[day]:
                toAdd = i
        sortedArr.pop(toRemove)
        if toRemove >= toAdd:
            sortedArr.insert(toAdd, expenditure[day])
        else:
            sortedArr.insert(toAdd - 1, expenditure[day])
    return count


print activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5)
