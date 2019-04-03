# 338. 比特位计数
# https://leetcode-cn.com/problems/counting-bits/

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            result[i] = result[i&(i-1)] + 1
        return result


s = Solution()
print(s.countBits(2))