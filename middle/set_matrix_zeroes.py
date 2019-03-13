# 73. 矩阵置零
# https://leetcode-cn.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        firstCol = False
        firstRow = False

        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                firstCol = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstRow = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if firstCol:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        if firstRow:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        print(matrix)

s = Solution()
print(s.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))