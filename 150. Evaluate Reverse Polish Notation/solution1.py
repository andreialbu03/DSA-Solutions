import operator

def func(tokens):
    stack = []

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b)
    }

    for token in tokens:
        if token in "+-*/":
            right = stack.pop()
            left = stack.pop()
            result = ops[token](left, right)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]

    # stack = []

    # for char in  tokens:
    #     if char == "+":
    #         stack.append(stack.pop() + stack.pop())
    #     elif char == "-":
    #         right = stack.pop()
    #         left = stack.pop()
    #         stack.append(left - right)
    #     elif char == "*":
    #         stack.append(stack.pop() * stack.pop())
    #     elif char == "/":
    #         right = stack.pop()
    #         left = stack.pop()
    #         stack.append(int(left / right))
    #     else:
    #         stack.append(int(char))

    # return stack[0]

print(func(["4","13","5","/","+"]))