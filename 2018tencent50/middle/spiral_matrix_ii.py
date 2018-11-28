# 螺旋矩阵II
# https://leetcode-cn.com/problems/spiral-matrix-ii/

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for _ in range(n)] for _ in range(n)]

        round = n // 2
        index = 1
        for i in range(0, round):
            width = n-1-i*2
            for j in range(0, width):
                result[i][j+i] = index
                result[j+i][width+i] = index + width
                result[n - 1 - i][n - 1 - j - i] = index + width*2
                result[n - 1 - j - i][i] = index + width*3
                index+=1
            index = index + width*3
        if n % 2 == 1:
            result[round][round] = n * n

        return result

s = Solution()
result = s.generateMatrix(5)
for cow in result:
    print(cow)