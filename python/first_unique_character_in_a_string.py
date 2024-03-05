class Solution:
    def firstUniqChar(self, s: str) -> int:
        str_dict = {}
        for c in s:
            if(c in str_dict):
                str_dict[c]+=1
            else:
                str_dict[c] = 1

        for key in str_dict:
            if(str_dict[key] == 1):
                return s.index(key)
        return -1