# 1017. 负二进制转换
# https://leetcode-cn.com/problems/convert-to-base-2/


class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return "0"
        result = []
        while N != 0:
            a = abs(N % -2)
            result.append(str(int(a)))
            N = (N - a) / -2
        result.reverse()
        return "".join(result)

s = Solution()
print(s.baseNeg2(3))