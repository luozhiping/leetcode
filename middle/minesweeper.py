# 529. 扫雷游戏
# https://leetcode-cn.com/problems/minesweeper/

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        queue = [click]

        direction = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]

        while queue:
            MCount = 0

            c = queue.pop(0)

            ECount = 0
            for dir in direction:
                pos = [c[0]+dir[0], c[1]+dir[1]]
                if 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0]):
                    if board[pos[0]][pos[1]] == 'M':
                        MCount += 1
                    elif board[pos[0]][pos[1]] == 'E':
                        if pos not in queue:
                            queue.append(pos)
                            ECount += 1
            if MCount == 0:
                board[c[0]][c[1]] = 'B'
            else:
                board[c[0]][c[1]] = str(MCount)
                if ECount > 0:
                    queue = queue[:-ECount]
        return board



s = Solution()
print(s.updateBoard(
[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
,[1,2]))