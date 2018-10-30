# nim游戏
# https://leetcode-cn.com/problems/nim-game/


class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # result = []
        # result.append(True)
        # result.append(True)
        # result.append(True)
        # result.append(True)
        # result.append(False)
        # for i in range(5, n+1):
        #     result.append(not(result[i-1] and result[i-2] and result[i-3]))
        # return result[n]
        return n % 4 != 0;

s = Solution()
print(s.canWinNim(5))