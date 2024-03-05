class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        concats = set([])
        for word in words:
            code = ""
            for c in word:
                code = code + morse[ord(c)-97]
            concats.add(code)
        return len(concats)