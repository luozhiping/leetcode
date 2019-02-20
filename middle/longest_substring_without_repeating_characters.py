# 3. 无重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        if len(s) == 1:
            return 1
        start = 0
        maxLength = 0
        mark = {}
        for index, c in enumerate(s):
            if c in mark:
                if mark[c] < start:
                    mark[c] = index
                    l = index - start + 1
                    if maxLength < l:
                        maxLength = l
                else:
                    l = index - start
                    if maxLength < l:
                        maxLength = l
                    start = mark[c] + 1
                    mark[c] = index
            else:
                mark[c] = index
                l = index - start + 1
                if maxLength < l:
                    maxLength = l

        return maxLength



s = Solution()
print(s.lengthOfLongestSubstring("tmmzuxt"))