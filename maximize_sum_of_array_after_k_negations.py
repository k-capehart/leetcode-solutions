class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        min = 100000
        index = 0
        for i in range(K):
            if A[i] < min:
                A[i] = -A[i]
                min = A[i]
                index = i
            else:
                A[index] = -A[index]
        return sum(A)