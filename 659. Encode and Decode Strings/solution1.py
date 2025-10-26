class Solution:
    def encode(self, strs):
        # write your code here
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output

    def decode(self, str):
        # write your code here
        output = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            word = str[j+1:j + length+1]
            output.append(word)
            i = j + length + 1

        return output