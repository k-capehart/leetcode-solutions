class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        str_len = len(A[0])
        res = 0
        for i in range(0, str_len):
            for x in range(1, len(A)):
                if ord(A[x][i]) < ord(A[x-1][i]):
                    res+=1
                    break
        return res