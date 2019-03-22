# 306. 累加数
# https://leetcode-cn.com/problems/additive-number/


class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def calNext(num, pre1, pre2):
            num3 = pre1 + pre2
            tmp = str(num3)
            if tmp == num:
                return True
            if len(tmp) >= len(num):
                return False
            if num[:len(tmp)] == tmp:
                return calNext(num[len(tmp):], pre2, num3)
            return False


        for i in range(1, len(num) // 2 + 1):
            if num[0] == '0' and i > 1:
                return False
            num1 = int(num[:i])
            j = 1
            while j + i < (len(num) + i) // 2 + 1:
                if num[i] == '0' and j > 1 :
                    j += 1
                    continue
                num2 = int(num[i:i+j])
                if calNext(num[i+j:], num1, num2):
                    return True
                j += 1
        return False



s = Solution()
print(s.isAdditiveNumber("000"))