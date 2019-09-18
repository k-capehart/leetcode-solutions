class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            count+=n%2
            n = n/2
        return count