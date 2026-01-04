def func(temperatures):
    stack = []
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            last_index = stack.pop()
            res[last_index] = i - last_index
        
        stack.append(i)
    return res


    # stack = []

    # for i in range(len(temperatures)):
    #     warmerDay = False
    #     for k in range(i+1, len(temperatures)):
    #         if temperatures[k] > temperatures[i]:
    #             warmerDay = True
    #             stack.append(k-i)
    #             break
    #     if not warmerDay:
    #         stack.append(0)
    # return stack

print(func([30,40,50,60]))