from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        len1 = len(word1)
        len2 = len(word2)

        if (len1 != len2):
            return False

        if (set(word1) != set(word2)):
            return False

        char_dict1 = Counter(word1)
        char_dict2 = Counter(word2)

        if (sorted(char_dict1.values()) != sorted(char_dict2.values())):
            return False

        return True
