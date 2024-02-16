'''
Generate all the permuation of a string
'''
def generatePermutation(added, pending):
    if len(pending) == 0:
        return [''.join(added)]
    outArr = []
    for i, ele in enumerate(pending):
        outArr.extend(generatePermutation(added + [ele], pending[:i] + pending[i+1:]))
    return outArr


if __name__ == '__main__':
    s = 'ABC'
    print generatePermutation([], list(s))
