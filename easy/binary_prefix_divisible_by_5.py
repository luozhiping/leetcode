# 1018. 可被 5 整除的二进制前缀
# https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/

class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        result = [False for _ in range(len(A))]
        num = 0
        for i in range(len(A)):
            num = num * 2 + A[i]
            result[i] = num % 5 == 0
        return result


s = Solution()
print(s.prefixesDivBy5([0,1,1,1,1,1]))