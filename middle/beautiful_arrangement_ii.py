# 667. 优美的排列 II
# https://leetcode-cn.com/problems/beautiful-arrangement-ii/

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        start = k + 1

        up = 1
        down = start
        while abs(up - down) >= 2:
            result.append(up)
            result.append(down)
            up += 1
            down -= 1
        if k % 2 == 0:
            result.append(up)
        else:
            result.append(up)
            result.append(down)
        result.extend([i for i in range(start+1, n+ 1)])
        return result


s = Solution()
print(s.constructArray(100, 25))