def func(nums):
    nums.sort()
    a = 0
    res = []
    
    while a < len(nums) - 2:
        if a > 0 and nums[a] == nums[a-1]:
            a += 1
            continue
        b = a + 1
        c = len(nums) - 1
        while b < c:
            total = nums[a] + nums[b] + nums[c]
            if total == 0:
                res.append([nums[a], nums[b], nums[c]])
                # b, c = b + 1, c - 1
                b += 1
                while b < c and nums[b] == nums[b - 1]:
                    b += 1
            elif total > 0:
                c -= 1
            else:
                b += 1
        a += 1

    return res

print(func([-1,0,1,2,-1,-4]))