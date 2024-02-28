from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        len1 = len(word1)
        len2 = len(word2)

        if (len1 != len2):
            return False

        if (set(word1) != set(word2)):
            return False

        char_dict1 = defaultdict(int)
        char_dict2 = defaultdict(int)

        for i in range(len1):
            char_dict1[word1[i]] += 1
            char_dict2[word2[i]] += 1

        if (char_dict1.keys() != char_dict2.keys()):
            return False
