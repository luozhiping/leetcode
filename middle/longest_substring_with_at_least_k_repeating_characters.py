# 395. 至少有K个重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/

import re
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        self.result = 0

        def calcResult(subString):
            if len(subString) < k:
                return 0
            counts = {}
            for c in subString:
                counts[c] = counts.get(c, 0) + 1
            # print(counts)
            allAboveK = True
            split = []
            for c in counts:
                if counts[c] < k:
                    split.append(c)
            if split:
                # print("".join(split))
                splited = re.split("|".join(split), subString)
                for sub in splited:
                    if sub:
                        self.result = max(self.result, calcResult(sub))
            else:
                self.result = max(self.result, len(subString))

            return self.result
        calcResult(s)
        return self.result

s = Solution()
print(s.longestSubstring("abcdedghijklmnopqrstuvwxyz", 2))