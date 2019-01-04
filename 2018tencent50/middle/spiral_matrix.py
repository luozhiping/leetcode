# 螺旋矩阵
# https://leetcode-cn.com/problems/spiral-matrix/

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        up = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        result = []
        while True:
            for i in range(left, right+1):
                result.append(matrix[up][i])
            up += 1
            if up > bottom:
                break
            for i in range(up, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            if bottom < up:
                break
            for i in range(bottom, up-1, -1):
                result.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return result

s = Solution()
print(s.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))