class Solution:
    def groupAnagrams(self, strs):
        
        sortedWords = ["".join(sorted(x)) for x in strs]
        words = {}

        for i in range(len(sortedWords)):
            if sortedWords[i] in words:
                words[sortedWords[i]].append(strs[i])
            else:
                words[sortedWords[i]] = [strs[i]]
            
        return list(words.values())