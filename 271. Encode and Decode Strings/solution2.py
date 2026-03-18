class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i])) + "#" + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while i < len(s)
            j = i
            length = ""
            while s[j] != "#":
                length +=  s[j]
                j += 1
            length = int(length)
            word = s[j+1:j+length+1]
            res.append(word)
            i += j + length + 1
        return res