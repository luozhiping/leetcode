# 387. 字符串中的第一个唯一字符
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabets = {}
        for c in s:
            if c in alphabets:
                alphabets[c] = alphabets[c] + 1
            else:
                alphabets[c] = 1
        for index, c in enumerate(s):
            if alphabets[c] == 1:
                return index
        return -1

s = Solution()
print(s.firstUniqChar("loveleetcode"))