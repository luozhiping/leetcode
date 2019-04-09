# 91. 解码方法
# https://leetcode-cn.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0

        board1 = [0 for _ in range(len(s))]
        board2 = [0 for _ in range(len(s))]
        board1[0] = 1
        for i in range(1, len(s)):
            if s[i] == "0":
                board1[i] = 0
            else:
                board1[i] = board1[i - 1] + board2[i - 1]
            if int(s[i-1:i+1]) <= 26:
                board2[i] = board1[i - 1]
            else:
                board2[i] = 0
        return board2[-1] + board1[-1]



s = Solution()
print(s.numDecodings("111010"))