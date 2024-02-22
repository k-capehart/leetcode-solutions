class Solution:
    count = 0
    rev_count = 0
    def diStringMatch(self, S: str) -> List[int]:
        def increaseDecrease(i):
            if i == 'I':
                res = self.count
                self.count+=1
            else:
                res = self.rev_count
                self.rev_count-=1
            return res
        
        self.rev_count = len(S)
        res = [increaseDecrease(i) for i in S]
        res.append(self.count)
        
        return res