def func(nums, k):
    freq_dict = {}

    for num in nums:
        freq_dict[num] = 1 + freq_dict.get(num, 0)

    freq_list = [[] for i in range(len(nums)+1)]

    for k, v in freq_dict.items():
        freq_list[v].append(k)

    # print(freq_list)

    result = []
    for i in range(len(freq_list) -1, 0, -1):
        for num in freq_list[i]:
            result.append(num)
            print(len(result))
            if len(result) == k:
                return result
            
print(func([1,1,1,2,2,3], 2))