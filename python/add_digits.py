class Solution(object):
    def addDigits(self, num):
        while len(str(num)) > 1:
            sum = 0
            ls = [int(x) for x in str(num)]
            for x in ls:
                sum += x
            num = sum
        return num
