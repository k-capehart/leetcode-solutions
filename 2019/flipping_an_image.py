class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in A:
            row = []
            for j in i:
                if j == 1:
                    row = [0] + row
                else:
                    row = [1] + row
            res.append(row)
        return res