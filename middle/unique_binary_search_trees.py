# 96.不同的二叉搜索树
# https://leetcode-cn.com/problems/unique-binary-search-trees/

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0 for i in range(n+1)]

        count[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                c = count[j] * count[i - 1 - j]
                count[i] = count[i] + c
        return count[n]

s = Solution()
print(s.numTrees(1))