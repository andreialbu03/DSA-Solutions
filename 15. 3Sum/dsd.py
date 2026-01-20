class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = 0
        b = a + 1
        c = len(nums) - 1
        res = []

        while a < len(nums) - 3:
            while b < c:
                if a > 0 and nums[a] == nums[a-1]:
                    break
                add = nums[a] + nums[b] + nums[c]
                if add > 0:
                    c -= 1
                elif add < 0:
                    b += 1
                else:
                    res.append([nums[a], nums[b], nums[c]])
            a += 1
        return res