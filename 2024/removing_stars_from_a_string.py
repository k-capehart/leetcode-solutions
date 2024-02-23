class Solution(object):
    def removeStars(self, s):      
        chars = []

        for char in s:
            if char is not '*':
                chars.append(char)
            else:
                chars.pop()
        return "".join(chars)