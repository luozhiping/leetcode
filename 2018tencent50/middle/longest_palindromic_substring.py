# 最长回文子串
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/

class Solution(object):


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #计算1字母回文
        if len(s) == 0:
            return ""
        else:
            max = s[0]
        for i in range(0, len(s)):
            if i*2+1 < len(max) or ((len(s)-i-1)*2+1) < len(max):
                print(i)
                continue
            #single
            offset = 1
            left = i - offset
            right = i + offset
            str = s[i]
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    str = s[left] + str + s[right]
                    offset+=1
                    left = i - offset
                    right = i + offset
                else:
                    break
            if len(max) <= len(str):
                max = str
            #double
            if i == len(s) - 1:
                continue
            if s[i] == s[i+1]:
                offset = 1
                left = i - offset
                right = i+1 + offset
                str = s[i]+s[i+1]
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        str = s[left] + str + s[right]
                        offset += 1
                        left = i - offset
                        right = i + 1 + offset
                    else:
                        break
                if len(max) <= len(str):
                    max = str
        return max


s = Solution()
print(s.longestPalindrome("aaaaabb"))