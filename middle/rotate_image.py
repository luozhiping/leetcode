# 48. 旋转图像
# https://leetcode-cn.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n = len(matrix)
        # print((n+1)//2)
        for i in range((n+1)//2):
            for j in range(i, n - 1 - i):
                pos1 = [i, j]
                pos2 = [j, n - 1 - i]
                pos3 = [n - 1- i,n - 1 - j]
                pos4 = [n - 1 - j, i]
                # print(pos1, pos2, pos3, pos4)
                matrix[pos1[0]][pos1[1]],matrix[pos2[0]][pos2[1]],matrix[pos3[0]][pos3[1]],matrix[pos4[0]][pos4[1]]\
                    = matrix[pos4[0]][pos4[1]],matrix[pos1[0]][pos1[1]],matrix[pos2[0]][pos2[1]],matrix[pos3[0]][pos3[1]]
        # print(matrix)


s = Solution()
s.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])