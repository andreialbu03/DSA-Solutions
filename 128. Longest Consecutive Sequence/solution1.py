def func(nums):
        myset = set(nums)
        streak = 0

        for num in myset:
            if num - 1 not in myset:
                current_streak = 1
                current_num = num

                while (current_num + 1 in myset):
                    current_streak += 1
                    current_num += 1
                if current_streak > streak:
                    streak = current_streak

        return streak

nums = [100,4,200,1,3,2,5]
print(func(nums))