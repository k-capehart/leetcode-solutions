class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        divisor = len1
        possible = str1

        while (possible != ""):
            if len1 % divisor == 0 and len2 % divisor == 0:
                div1 = len1 // divisor
                div2 = len2 // divisor
                if possible * div1 == str1 and possible * div2 == str2:
                    return possible
            possible = possible[:-1]
            divisor -= 1
        return possible
