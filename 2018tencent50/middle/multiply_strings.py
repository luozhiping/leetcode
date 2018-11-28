# 字符串相乘
# https://leetcode-cn.com/problems/multiply-strings/

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        len1 = len(num1)
        len2 = len(num2)

        result = []

        for i in range(len2):
            carry = 0
            for j in range(len1):
                temp = int(num2[-1-i]) * int(num1[-1-j]) + carry
                # print(-1-j-i, i+j+1, len(result))
                if i+j+1 > len(result):
                    result.insert(0, temp % 10)
                    carry = temp // 10
                else:
                    temp = result[-1-j-i] + temp
                    result[-1-j-i] = temp % 10
                    carry = temp // 10

            if carry != 0:
                result.insert(0, carry)
        return ''.join([str(t) for t in result])


s = Solution()
print(s.multiply("12322", "454566"))