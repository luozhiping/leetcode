# 820. 单词的压缩编码
# https://leetcode-cn.com/problems/short-encoding-of-words/

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = set(words)
        s = '#'.join(words)+'#'
        le=len(s)
        for i in words:
            if s.count(i+'#')>1:
                le = le-len(i)-1
        return le

s = Solution()
print(s.minimumLengthEncoding(["time", "me", "bell"]))