class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        temp_row=[0]*m
        temp_col=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    temp_row[i]=1
                    temp_col[j]=1
        for i in range(m):
            for j in range(n):
                if temp_row[i]==1 or temp_col[j]==1:
                    matrix[i][j]=0
        return matrix