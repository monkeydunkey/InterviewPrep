'''
Find the longest common sequence in the given 2 stirngs
'''

def longSeq(str1, str2):
    arr = [[0 for x in xrange(len(str1) + 1)] for y in xrange(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str1[j-1] == str2[i-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    return arr[-1][-1]



if __name__ == '__main__':
    print longSeq('abcde', 'aecdf')
