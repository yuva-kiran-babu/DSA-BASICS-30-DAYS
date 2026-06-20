class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum = 0
        n = len(mat)
        for i in (range(n)):
            primary_diagonal_elements = mat[i][i]
            total_sum += primary_diagonal_elements
            secondary_diagonal_elements = mat[i][n-1-i]
            total_sum += secondary_diagonal_elements
        if len(mat) % 2 != 0:
            total_sum -= mat[n//2][n//2]

        return total_sum