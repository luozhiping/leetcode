# 77. 组合
# https://leetcode-cn.com/problems/combinations/

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1, n+1):
            result.extend(self.combineList([i], n, k - 1))
        return result

    def combineList(self, r, n, k):
        result = []
        if k >= 1:
            for i in range(r[len(r) - 1], n + 1):
                if i in r:
                    continue
                l = list(r)
                l.append(i)
                result.extend(self.combineList(l, n, k - 1))
        else:
            result = [r]
        return result


s = Solution()
print(s.combine(4, 2))