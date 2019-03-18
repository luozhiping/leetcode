# 440. 字典序的第K小数字
# https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cur = 1
        k -= 1
        while k > 0:
            step = 0
            first = cur
            last = cur + 1
            while first <= n:
                step += min(n+1, last) - first
                first *= 10
                last *= 10
            if step <= k:
                cur += 1
                k -= step
            else:
                cur *= 10
                k -= 1
        return cur

s = Solution()
print(s.findKthNumber(13, 2))