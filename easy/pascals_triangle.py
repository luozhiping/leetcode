# 118. 杨辉三角
# https://leetcode-cn.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            length = i + 1
            tmp = [1 for _ in range(length)]
            for j in range(1, length - 1):
                tmp[j] = result[i-1][j] + result[i-1][j-1]
            result.append(tmp)
        return result

s = Solution()
print(s.generate(5))