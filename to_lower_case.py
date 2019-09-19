class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for i in str:
            if i.isupper():
                res = res + chr(ord(i) + 32)
            else:
                res = res + i
        return res