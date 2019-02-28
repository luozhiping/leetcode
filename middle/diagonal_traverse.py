# 498. 对角线遍历
# https://leetcode-cn.com/problems/diagonal-traverse/

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction = 0
        cur = [0, 0]
        if not matrix:
            return []
        M = len(matrix)
        N = len(matrix[0])
        if M == 0 or N == 0:
            return []
        result = []
        while cur[0] != M-1 or cur[1] != N-1:
            result.append(matrix[cur[0]][cur[1]])
            if direction == 0:
                tmp = [cur[0]-1, cur[1]+1]
                if tmp[0] < 0:
                    tmp[0] = 0
                    direction = 1
                if tmp[1] >= N:
                    tmp[1] = cur[1]
                    tmp[0] = cur[0] + 1
                    direction = 1
                cur = tmp
            else:
                tmp = [cur[0] + 1, cur[1] - 1]
                if tmp[1] < 0:
                    tmp[1] = 0
                    direction = 0
                if tmp[0] >= M:
                    tmp[0] = cur[0]
                    tmp[1] = cur[1] + 1
                    direction = 0
                cur = tmp
        result.append(matrix[cur[0]][cur[1]])
        return result

s = Solution()
print(s.findDiagonalOrder(
    [
        [1, 2, 3]
    ]
))