def func(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not validAlphaNum(s[left]):
            left += 1
        while right > left and not validAlphaNum(s[right]):
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
        
    # newString = ""

    # for c in s:
    #     if c.isalnum():
    #         newString += c.lower()
    
    # return newString == newString[::-1]

def validAlphaNum(c):
    return (ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9"))

print(func(".,"))