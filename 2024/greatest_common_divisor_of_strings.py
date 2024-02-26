class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        if str1 + str2 != str2 + str1:
            return ""

        len1 = len(str1)
        len2 = len(str2)

        divisor = len1 // 2 if len1 > len2 else len2 // 2

        while (divisor > 0):
            if len1 % divisor == 0 and len2 % divisor == 0:
                if str1[:divisor] == str2[:divisor]:
                    return str1[:divisor]
            divisor -= 1
        return ""
