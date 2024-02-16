def long_increasing_seq(s1):
    arr = [1 for x in xrange(len(s1))]
    for i, e in enumerate(s1):
        for j in xrange(i):
            if e > s1[j]:
                arr[i] = max(arr[i], arr[j] + 1)
    print arr
    return max(arr)

def findNumberOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return long_increasing_seq(nums)

if __name__ == '__main__':
    print findNumberOfLIS([1,3,5,4,7])
    print [10, 22, 9, 33, 21, 50, 41, 60, 80], long_increasing_seq([10, 22, 9, 33, 21, 50, 41, 60, 80])
    print [3, 10, 2, 1, 20], long_increasing_seq([3, 10, 2, 1, 20])
    print [1,3,5,4,7], long_increasing_seq([1,3,5,4,7])
    print [50, 3, 10, 7, 40, 80], long_increasing_seq([50, 3, 10, 7, 40, 80])
