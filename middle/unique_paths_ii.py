# 63. 不同路径 II
# https://leetcode-cn.com/problems/unique-paths-ii/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        # board = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        last = [0 for _ in range(len(obstacleGrid[0]))]
        for i in range(len(obstacleGrid)):
            cur = [0 for _ in range(len(obstacleGrid[0]))]
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    cur[0] = 1
                    continue
                if obstacleGrid[i][j] == 1:
                    continue
                left = j - 1
                top = j
                leftValue = 0
                if j > 0:
                    if obstacleGrid[i][j - 1] != 1:
                        leftValue = cur[j - 1]
                    else:
                        leftValue = 0
                topValue = 0
                if i > 0:
                    if obstacleGrid[i-1][j] != 1:
                        topValue = last[j]
                    else:
                        topValue = 0
                cur[j] = leftValue + topValue
            last = cur
        # print(board)
        return cur[-1]

        #
        # start = [0, 0]
        # end = [len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1]
        # # print('start')
        # seq = [start]
        # dirs = [[0, 1], [1, 0]]
        # board[0][0] = 1
        # while seq:
        #     cur = seq.pop(0)
        #     tmp = []
        #     for dir in dirs:
        #         next = [cur[0] + dir[0], cur[1] + dir[1]]
        #         if next[0] == len(obstacleGrid) or next[1] == len(obstacleGrid[0]) or obstacleGrid[next[0]][next[1]] == 1:
        #             continue
        #
        #         board[next[0]][next[1]] += 1
        #         tmp.append(next)
        #         print(next)
        #     seq.extend(tmp)
        # return board[-1][-1]

s = Solution()
print(s.uniquePathsWithObstacles([
  [1, 0]
]))


import random
testW = random.randint(3, 20)
testH = random.randint(3, 20)
test = []
for i in range(testW):
    t = []
    for j in range(testH):
        if random.random() > 0.8:
            t.append(1)
        else:
            t.append(0)
    test.append(t)
test[0][0] = 0
test[-1][-1] = 0
print(test)
# test = [[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],[1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]]
print(s.uniquePathsWithObstacles(test))