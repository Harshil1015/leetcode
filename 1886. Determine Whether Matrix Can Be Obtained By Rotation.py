class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        match_0 = True  # 0 degrees
        match_90 = True  # 90 degrees
        match_180 = True  # 180 degrees
        match_270 = True  # 270 degrees

        for i in range(n):
            for j in range(n):
                if mat[i][j] != target[i][j]:
                    match_0 = False
                if mat[i][j] != target[j][n - 1 - i]:
                    match_90 = False
                if mat[i][j] != target[n - 1 - i][n - 1 - j]:
                    match_180 = False
                if mat[i][j] != target[n - 1 - j][i]:
                    match_270 = False

        return match_0 or match_90 or match_180 or match_270
