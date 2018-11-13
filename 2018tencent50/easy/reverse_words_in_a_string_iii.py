# 反转字符串中的单词 III
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        words = s.split()[::-1]
        result = ""
        for word in words:
            result += word + " "
        return result.strip()



s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))