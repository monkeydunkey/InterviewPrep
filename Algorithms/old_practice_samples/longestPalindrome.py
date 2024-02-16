'''
Find the longest palindrome in the given string
'''

def findPalindrome(s):
    arr = [[False for x in xrange(len(s))] for y in xrange(len(s))]
    startInd, endInd, maxTillNow = None, None, None
    for i in range(len(s) - 1, -1, -1):
        for j in range(len(s) - 1, i - 1, -1):
            if s[i] == s[j]:
                if i+1 < j-1:
                    arr[i][j] = arr[i+1][j-1]
                    if (maxTillNow is None or j - i > maxTillNow) and arr[i][j]:
                        startInd = i
                        endInd = j
                        maxTillNow = j - i
                else:
                    arr[i][j] = True
		    if maxTillNow is None or j - i > maxTillNow:
                        startInd = i
                        endInd = j
                        maxTillNow = j - i
    return s[startInd:endInd+1]


if __name__ == "__main__":
    print findPalindrome('aaaabbaa')
    
    
