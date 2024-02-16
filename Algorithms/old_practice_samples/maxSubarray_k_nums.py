'''
Largest sum subarray with at-least k numbers
'''

def maxSumWithKNums(arr, k):
    maxSum = None
    startInd = 0
    endInd = startInd + k
    while endInd < len(arr) + 1:
        tempSum = reduce(lambda x,y: x+y, arr[startInd: endInd])
        if maxSum is None or tempSum > maxSum:
            maxSum = tempSum
            endInd += 1
        if tempSum < 0:
            startInd = endInd - 1
            endInd = startInd + k
    return maxSum


if __name__ == '__main__':
    print maxSumWithKNums([5 ,7 ,-9 ,3 ,-4 ,2 ,1 ,-8 ,9 ,10], 5)
