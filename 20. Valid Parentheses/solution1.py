def func(s):

    dic = {
            ")": "(",
            "}": "{",
            "]": "["
        }
    if len(s) < 2:
        return False
    
    stack = []
    for bracket in s:
        if bracket in dic and stack:
            popped = stack.pop()
            if popped != dic[bracket]:
                return False
        else:
            stack.append(bracket)
    
    if stack:
        return False
    return True


s = "(])"
# s = "(("

print(func(s))