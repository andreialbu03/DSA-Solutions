class Solution:
    def triangleType(self, nums: List[int]) -> str:

        if ((nums[0] + nums[1] <= nums[2]) or
            (nums[0] + nums[2] <= nums[1]) or
            (nums[1] + nums[2] <= nums[0])):
            return "none"

        freq_dic = {}
        for i in range(len(nums)):
            freq_dic[nums[i]] = 1 + freq_dic.get(nums[i], 0)
        
        if len(list(freq_dic)) == 3:
            return "scalene"
        elif len(list(freq_dic)) == 2:
            return "isosceles"
        else:
            return "equilateral"