class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        evens = [x for x in A if x % 2 == 0]
        odds = [x for x in A if x % 2 == 1]
        res = [0] * len(A)
        res[::2] = evens
        res[1::2] = odds
        return res