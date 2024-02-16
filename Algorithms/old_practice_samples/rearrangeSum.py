'''
Rearrange a string in sorted order followed by the integer sum
'''
from string import ascii_uppercase

def reArrange(s):
    charArr = {}
    for a in ascii_uppercase:
        charArr[a] = 0
    sumVal = 0
    for a in s:
        try:
            sumVal += int(a)
        except Exception as e:
            charArr[a] += 1

    outStr = ''
    for a in ascii_uppercase:
        outStr += a*charArr[a]
    outStr += str(sumVal)
    return outStr



if __name__ == '__main__':
    print reArrange('AC2BEW3')

