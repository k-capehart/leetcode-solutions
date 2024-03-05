class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balon = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for c in text:
            if c in balon:
                balon[c] += 1
        return min([ balon['b'], balon['a'], balon['l']//2, balon['o']//2, balon['n'] ])