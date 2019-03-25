# 424. 替换后的最长重复字符
# https://leetcode-cn.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        count = {}
        maxC = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxC = max(count[s[right]], maxC)
            while right - left + 1 - maxC > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

s = Solution()
print(s.characterReplacement("", 2))