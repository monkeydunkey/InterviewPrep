def check_balanced(st):
    stack = []
    opening = ['{', '(', '[']
    closing = ['}', ')', ']']
    for c in st:
        if c in opening:
            stack.append(c)
        elif c in closing:
            if len(stack) and c == closing[opening.index(stack[-1])]:
                stack.pop()
            else:
                return False
        else:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    #tests
    print '}{}', check_balanced('}{}')
    print '{([]))', check_balanced('{([]))')
    print '([])', check_balanced('([])')
    print '(({}', check_balanced('(({}')

