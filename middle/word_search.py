# 79. 单词搜索
# https://leetcode-cn.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        start = []
        for i, cols in enumerate(board):
            for j, row in enumerate(cols):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    start.append((i, j))
                    result = self.beginSearchPath((i, j), board, word[1:], board)
                    if result:
                        return True

        return False

    def beginSearchPath(self, start, board, word, mask):
        tmp = mask[start[0]][start[1]]
        mask[start[0]][start[1]] = None
        directs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for dir in directs:
            x = start[0] + dir[0]
            y = start[1] + dir[1]
            if x < 0 or x >= len(board):
                continue
            elif y < 0 or y >= len(board[x]):
                continue
            if mask[x][y] == word[0]:
                if len(word) == 1:
                    return True
                else:
                    result = self.beginSearchPath((x, y), board, word[1:], mask)
                    if result:
                        return True
        mask[start[0]][start[1]] = tmp
        return False



s = Solution()
# print(s.exist(
#     [["C", "A", "A"],
#      ["A", "A", "A"],
#      ["B", "C", "D"]]
# , "AAB"))

print(s.exist(
    [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

    , "ABCCED"))