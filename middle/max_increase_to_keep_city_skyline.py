# 807. 保持城市天际线
# https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline/

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        maxTop = [0 for _ in range(len(grid))]
        maxLeft = [0 for _ in range(len(grid))]
        for i in range(len(grid)):
            top = 0
            left = 0
            for j in range(len(grid)):
                top = max(top, grid[j][i])
                left = max(left, grid[i][j])
            maxTop[i] = top
            maxLeft[i] = left
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                result += max(min(maxLeft[i], maxTop[j]) - grid[i][j], 0)
        return result
s = Solution()
print(s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))