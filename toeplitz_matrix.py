class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        prev_row = matrix[0]
        row_length = len(matrix[0])
        for i in range(1, len(matrix)):
            for j in range(1, row_length):
                if matrix[i][j] != prev_row[j-1]:
                    return False
            prev_row = matrix[i]
        return True