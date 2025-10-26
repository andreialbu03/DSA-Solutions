class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for i in range(len(nums)):
            freq_dict[nums[i]] = 1 + freq_dict.get(nums[i], 0)
        
        freq_list = [[] for _ in range(len(nums)+1)]
        for c,v in freq_dict.items():
            freq_list[v].append(c)


        output = []
        for i in range(len(freq_list)-1,0, -1):
            for n in freq_list[i]:
                output.append(n)
                if len(output) == k:
                    return output