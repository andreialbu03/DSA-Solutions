def func(target, position, speed):
    pairs = [[p,s] for p, s in zip(position, speed)]
    stack = []

    for p, s in sorted(pairs)[::-1]:
        arrival = (target - p) / s
        if stack and stack[-1] >= arrival:
            continue
        stack.append(arrival)

    return len(stack)

print(func(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))