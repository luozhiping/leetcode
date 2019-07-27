# 695. 岛屿的最大面积
# https://leetcode-cn.com/problems/max-area-of-island/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        row = len(grid)
        col = len(grid[0])
        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = 1
                    seq = [(i, j)]
                    grid[i][j] = -1
                    while seq:
                        cur = seq.pop(0)
                        for dir in dirs:
                            nextPos = (cur[0]+dir[0], cur[1]+dir[1])
                            # print(nextPos, len(grid), len(grid[0]), nextPos[1] == len(grid[0]))
                            if nextPos[0] < 0 or nextPos[0] == row or nextPos[1] < 0 or nextPos[1] == col \
                                    or grid[nextPos[0]][nextPos[1]] != 1:
                                continue
                            grid[nextPos[0]][nextPos[1]] = -1
                            area += 1
                            seq.append(nextPos)
                    result = max(result, area)
        return result


s = Solution()
assert s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6
assert  s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0

import random
test = []
row = random.randint(40, 50)
for i in range(random.randint(40, 50)):
    t = []
    for j in range(row):
        t.append(random.randint(0, 1))
    test.append(t)
print(test)
s.maxAreaOfIsland(test)