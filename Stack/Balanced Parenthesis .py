def isBalanced(string):
    s = []
    for char in string:
        if char in '({{':
            s.append(char)
        elif char == '(':
            if not s or s[-1]!=')':
                return False
            s.pop()
        elif char == '}':
            if not s or s[-1]!='{':
                return False
            s.pop()
        elif char == ']':
            if not s or s[-1]!='[':
                return False
            s.pop()

    if not s:
        return False
    return True
    if not s:
        return True
    return False

string = input()
ans = isBalanced(string)
print(ans)