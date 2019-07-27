# 542. 01 矩阵
# https://leetcode-cn.com/problems/01-matrix/

import sys
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        board = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = -1
                    zero = [[i, j]]
                    seq = [[i, j]]
                    while seq:
                        cur = seq.pop(0)
                        for dir in dirs:
                            nextPos = [cur[0]+dir[0], cur[1]+dir[1]]
                            if nextPos[0] < 0 or nextPos[0] == len(matrix) or nextPos[1] < 0 or nextPos[1] == len(matrix[0]):
                                continue
                            if matrix[nextPos[0]][nextPos[1]] == 0:
                                matrix[nextPos[0]][nextPos[1]] = -1
                                zero.append(nextPos)
                                seq.append(nextPos)
                    zeros.append(zero)
        # print(zero)
        while True:
            allBlank = True
            for i, zero in enumerate(zeros):
                tmp = []
                for cur in zero:
                    for dir in dirs:
                        nextPos = [cur[0] + dir[0], cur[1] + dir[1]]
                        if nextPos[0] < 0 or nextPos[0] == len(matrix) or nextPos[1] < 0 or nextPos[1] == len(
                                matrix[0]):
                            continue
                        if matrix[nextPos[0]][nextPos[1]] == 1:
                            board[nextPos[0]][nextPos[1]] = board[cur[0]][cur[1]] + 1
                            matrix[nextPos[0]][nextPos[1]] = -1
                            tmp.append(nextPos)
                zeros[i] = tmp
                if tmp:
                    allBlank = False
            if allBlank:
                print(board)
                return board
s = Solution()
assert s.updateMatrix([[0,0,0,0],
                       [0,1,1,1],
                       [1,1,1,1]]) == [[0,0,0],[0,1,0],[0,0,0]]