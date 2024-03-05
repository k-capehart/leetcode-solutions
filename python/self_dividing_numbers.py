class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def checkDivs(x):
            for i in str(x):
                if int(i) == 0:
                    return False
                elif x % int(i) != 0:
                    return False
            return True
        
        return [x for x in range(left, right+1) if checkDivs(x)]