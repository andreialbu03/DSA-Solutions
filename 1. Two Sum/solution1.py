class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffDict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in diffDict:
                return i, diffDict[diff]
            
            diffDict[nums[i]] = i