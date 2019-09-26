class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = ['q','w','e','r','t','y','u','i','o','p']
        row2 = ['a','s','d','f','g','h','j','k','l']
        row3 = ['z','x','c','v','b','n','m']
        res = []
        words1 = []
        words2 = []
        def checkWords(words, row, next_words):
            for word in words:
                all_in = True
                for c in word.lower():
                    if c not in row:
                        all_in = False
                        break
                if all_in : res.append(word)
                else: next_words.append(word)
            return next_words
        checkWords(words, row1, words1)
        checkWords(words1, row2, words2)
        checkWords(words2, row3, words1)

        return res