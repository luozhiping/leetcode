# 151. 翻转字符串里的单词
# https://leetcode-cn.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        strs = s.strip().split(" ")
        result = []
        for i in range(len(strs) - 1, -1, -1):
            if strs[i]:
                result.append(strs[i])
        return " ".join(result)



s = Solution()
assert s.reverseWords("the sky is blue") == "blue is sky the"
assert s.reverseWords("a good   example") == "example good a"
assert s.reverseWords("  hello world!  ") == "world! hello"