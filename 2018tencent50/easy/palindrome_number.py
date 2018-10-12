# 回文数
# https://leetcode-cn.com/problems/palindrome-number/description/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        is_palindrome = True
        if len(x) == 0:
            return False
        if len(x) == 1:
            return True
        if len(x) % 2 == 0:
            left = len(x) // 2 - 1
            right = len(x) // 2
            while left >= 0:
                if x[left] != x[right]:
                    is_palindrome = False
                    break
                left -= 1
                right += 1
        else:
            left = len(x) // 2 - 1
            right = len(x) // 2 + 1
            while left >= 0:
                if x[left] != x[right]:
                    is_palindrome = False
                    break
                left -= 1
                right += 1
        return is_palindrome


class Solution2(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        n = x
        m = n % 10
        n = n // 10
        new = m
        while n != 0:
            m = n % 10
            n = n // 10
            new = new * 10 + m
        return new == x


s = Solution()
print(s.isPalindrome(0))
