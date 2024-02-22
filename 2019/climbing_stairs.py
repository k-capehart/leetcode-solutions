class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):
            return 1
        if(n == 2):
            return 2
        
        steps = [1, 2, 3]
        
        for i in range(2, n):
            steps[2] = steps[1]
            steps[1] = steps[0] + steps[1]
            steps[0] = steps[2]
            
        return steps[1]