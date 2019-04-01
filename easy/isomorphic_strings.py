# 205. 同构字符串
# https://leetcode-cn.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False


        dictionaryA = {}
        dictionaryB = {}

        for i in range(len(s)):
            if s[i] not in dictionaryA:
                if t[i] in dictionaryB:
                    return False
                dictionaryA[s[i]] = t[i]
                dictionaryB[t[i]] = s[i]
            else:
                if dictionaryA[s[i]] != t[i]:
                    return False
        return True


s = Solution()
print(s.isIsomorphic("ab", "aa"))