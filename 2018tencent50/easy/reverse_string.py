# 反转字符串
# https://leetcode-cn.com/problems/reverse-string/


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join([s[i] for i in range(len(s) - 1, -1, -1)])

s = Solution()
print(s.reverseString("hello"))
