# 130. 被围绕的区域
# https://leetcode-cn.com/problems/surrounded-regions/

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    if board[i][j] == "O":
                        seq = [[i, j]]
                        board[i][j] = "#"
                        while seq:
                            cur = seq.pop(0)
                            for dir in dirs:
                                c = [cur[0] + dir[0], cur[1] + dir[1]]
                                if c[0] < 0 or c[0] == len(board) or c[1] < 0 or c[1] == len(board[0]):
                                    continue
                                if board[c[0]][c[1]] == "O":
                                    seq.append(c)
                                    board[c[0]][c[1]] = "#"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        return board

s = Solution()
print(s.solve([["X","X","O","X"],
               ["X","O","X","X"],
               ["X","O","O","X"],
               ["X","O","X","X"]]))