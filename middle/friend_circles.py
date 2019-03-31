# 547. 朋友圈
# https://leetcode-cn.com/problems/friend-circles/

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        def dfs(visited, i):
            visited[i] = True
            for j in range(i+1, len(M)):
                if visited[j] or M[i][j] == 0:
                    continue
                else:
                    dfs(visited, j)

        result = 0
        visited = [False for _ in range(len(M))]
        for i in range(len(M)):
            if visited[i]:
                continue
            else:
                dfs(visited, i)
            result += 1
        return result

s = Solution()
print(s.findCircleNum([
    [1,1,0],
     [1,1,0],
     [0,0,1]
]))