# 6. Z 字形变换
# https://leetcode-cn.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = ""
        cycle = 2 * numRows - 2
        for row in range(numRows):
            j = 0
            while j + row < len(s):
                result += s[j + row]
                if row != 0 and row != numRows - 1 and j + cycle - row < len(s):
                    result += s[j + cycle - row]
                j += cycle
        return result
s = Solution()
print(s.convert("LEETCODEISHIRING", 3))