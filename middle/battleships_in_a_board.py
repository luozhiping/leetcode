# 419. 甲板上的战舰
# https://leetcode-cn.com/problems/battleships-in-a-board/

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    seq = [[i, j]]
                    board[i][j] = "0"
                    result += 1
                    while seq:
                        cur = seq.pop(0)
                        for dir in dirs:
                            c = [cur[0] + dir[0], cur[1] + dir[1]]
                            if c[0] < 0 or c[0] == len(board) or c[1] < 0 or c[1] == len(board[0]):
                                continue
                            if board[c[0]][c[1]] == "X":
                                seq.append(c)
                                board[c[0]][c[1]] = "0"
        return result





s = Solution()
print(s.countBattleships([
    ["X",".",".","X"],
    [".",".",".","X"],
    ["X","X",".","X"]
]))