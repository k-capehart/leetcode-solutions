class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        xor = bin(x^y)
        for i in xor:
            if i == '1':
                count+=1
        return count