class Solution:
    def fib(self, N: int) -> int:
        fibs = [0,1]
        if N == 0 or N == 1:
            return N
        for i in range(N):
            fibs[i%2] = fibs[0] + fibs[1]
        return fibs[N%2]