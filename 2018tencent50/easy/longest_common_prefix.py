# 最长公共前缀
# https://leetcode-cn.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        index = 0
        p = ""
        while p is not None:
            p = None
            for s in strs:
                if index >= len(s):
                    p = None
                    break
                if p is None:
                    p = s[index]
                else:
                    if p == s[index]:
                        continue
                    else:
                        p = None
                        break
            index += 1
            if p is not None:
                prefix += p
        return prefix


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))