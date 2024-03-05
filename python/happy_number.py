class Solution:
    def isHappy(self, n: int) -> bool:
        squares = set([n])
        while n != 1:
            num = 0
            for dig in str(n):
                num += int(dig)*int(dig)
            if num in squares:
                return False
            squares.add(num)
            n = num
            
        return True