# 221. 最大正方形
# https://leetcode-cn.com/problems/maximal-square/

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        board = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    board[i][j] = 0
                elif matrix[i][j] == "1":
                    left = 0 if j == 0 else board[i][j - 1]
                    top = 0 if i == 0 else board[i - 1][j]
                    leftTop = 0 if i == 0 and j == 0 else board[i - 1][j - 1]
                    board[i][j] = min(left, top, leftTop) + 1
                    result = max(result, board[i][j])
        # print(board)
        return result ** 2

s = Solution()
print(s.maximalSquare(
    [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","0","1","0"]]
))
print(s.maximalSquare([["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]))
print(s.maximalSquare(
    [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","0","1","0"]]))