class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        peak = 0
        peak_index = 0
        for i in range(len(A)):
            if A[i] > peak:
                peak = A[i]
                peak_index = i
        return peak_index