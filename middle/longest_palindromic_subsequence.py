# 516. 最长回文子序列
# https://leetcode-cn.com/problems/longest-palindromic-subsequence/

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = len(s)
        # bp = [[0 for _ in range(length)] for _ in range(length)]
        last = [0 for _ in range(length)]
        current = [0 for _ in range(length)]
        # result = 1
        for i in range(length-1, -1, -1):
            current[i] = 1
            for j in range(i+1, length):
                if s[j] == s[i]:
                    current[j] = last[j-1] + 2
                    # result = max(result, bp[i][j])
                else:
                    current[j] = max(last[j], current[j-1])
            current, last = last, current
        return last[length-1]

s = Solution()
assert s.longestPalindromeSubseq("bbbab") == 4
assert s.longestPalindromeSubseq("cbbd") == 2