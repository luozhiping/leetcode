# 买卖股票的最佳时机
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) == 0:
            return 0
        Min = prices[0]
        res = 0
        for p in prices:
            res = max(res, p - Min)
            Min = min(Min, p)
        return res


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
