# 74. 搜索二维矩阵
# https://leetcode-cn.com/problems/search-a-2d-matrix/

class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i = 0
        j = len(matrix[i]) - 1
        while i < len(matrix) and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            return False
        length = len(matrix[0])
        # find row
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][length - 1]:
                break
            elif target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][length - 1]:
                left = mid + 1

        left = 0
        right = len(matrix[mid]) - 1
        while left <= right:
            midC = (left + right) // 2
            if matrix[mid][midC] == target:
                return True
            if matrix[mid][midC] < target:
                left = midC + 1
            else:
                right = midC - 1
        return False

s = Solution()
print(s.searchMatrix(
    [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ],30))