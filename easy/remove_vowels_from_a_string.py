# 1119. 删去字符串中的元音
# https://leetcode-cn.com/problems/remove-vowels-from-a-string/

class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        yuan = ['a','e','i','o','u']
        for y in yuan:
            S = S.replace(y, "")
        return S

s = Solution()
assert s.removeVowels("leetcodeisacommunityforcoders") == "ltcdscmmntyfrcdrs"
assert s.removeVowels("aeiou") == ""