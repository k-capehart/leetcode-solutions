import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = re.findall(r'\w+', paragraph) 
        word_map = {}
        
        for i in words:
            if i not in banned:
                if i in word_map:
                    word_map[i] = word_map[i] + 1
                else:
                    word_map[i] = 1
        return max(word_map, key=word_map.get)