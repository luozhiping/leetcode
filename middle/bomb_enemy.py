# 361. 轰炸敌人
# https://leetcode-cn.com/problems/bomb-enemy/

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "0":
                    continue
                enmy = 0
                for dir in dirs:
                    n = [i + dir[0], j + dir[1]]
                    while not (n[0] < 0 or n[0] == len(grid) or n[1] < 0 or n[1] == len(grid[0]) or grid[n[0]][n[1]] == "W"):
                        if grid[n[0]][n[1]] == "E":
                            enmy += 1
                        n = [n[0] + dir[0], n[1] + dir[1]]
                grid[i][j] = enmy
                result = max(result, enmy)
        return result

s = Solution()
print(s.maxKilledEnemies([
    ["0","E","0","0"],
    ["E","0","W","E"],
    ["0","E","0","0"]
]))