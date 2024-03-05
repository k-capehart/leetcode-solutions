class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        a_length = len(A)
        if A[int(a_length/2)] == A[a_length-1]:
            return A[int(a_length/2)]
        else:
            return A[int(a_length/2)-1]