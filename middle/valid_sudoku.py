# 36. 有效的数独
# https://leetcode-cn.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for _ in range(len(board))]
        cols = [{} for _ in range(len(board[0]))]
        boxes = [{} for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                box = i//3*3+j//3
                num = board[i][j]
                if num in rows[i]:
                    return False
                rows[i][num] = 1
                if num in cols[j]:
                    return False
                cols[j][num] = 1
                if num in boxes[box]:
                    return False
                boxes[box][num] = 1
        return True

s = Solution()
print(s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
))