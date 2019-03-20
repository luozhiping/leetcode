# 848. 字母移位
# https://leetcode-cn.com/problems/shifting-letters/

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        if not shifts or not S:
            return S
        count = sum(shifts)
        result = []
        for i in range(len(shifts)):
            re = count % 26
            des = ord(S[i]) + re
            if des > ord('z'):
                des = ord('a') + des - ord('z') - 1
            result.append(chr(des))
            count -= shifts[i]
        result.append(S[len(shifts):])
        return "".join(result)

s = Solution()
print(s.shiftingLetters("ruu",
[26,9,17]))