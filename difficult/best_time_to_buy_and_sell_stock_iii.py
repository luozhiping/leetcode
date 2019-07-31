# 123. 买卖股票的最佳时机 III
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        i = 0
        ahead = [0 for _ in range(len(prices))]
        goBack = [0 for _ in range(len(prices))]

        minValue = prices[0]
        for i in range(1, len(prices)):
            ahead[i] = max(ahead[i-1], prices[i]-minValue)
            minValue = min(minValue, prices[i])

        maxValue = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            goBack[i] = max(goBack[i+1], maxValue - prices[i])
            maxValue = max(maxValue, prices[i])
        # print(ahead, goBack)
        result = 0
        for i in range(1, len(prices)-1):
            result = max(result, ahead[i]+goBack[i+1])
        result = max(result, ahead[-1])
        result = max(result, goBack[0])
        return result
s = Solution()
assert s.maxProfit([3,3,5,0,0,3,1,4]) == 6
assert s.maxProfit([1,2,3,4,5]) == 4
assert s.maxProfit([7,6,4,3,1]) == 0
assert s.maxProfit([1,3]) == 2
assert s.maxProfit([0]) == 0
assert s.maxProfit([]) == 0
import random
test = []
for i in range(random.randint(100, 200)):
    test.append(random.randint(0, 100))
print(test)
test = [51, 46, 98, 21, 72, 98, 47, 96, 66, 20, 2, 31, 28, 93, 52, 40, 38, 9, 62, 55, 38, 56, 60, 10, 20, 39, 63, 30, 71, 39, 30, 86, 11, 96, 35, 6, 40, 22, 33, 97, 93, 60, 26, 37, 80, 31, 14, 50, 80, 91, 92, 63, 58, 68, 76, 44, 95, 15, 75, 70, 28, 34, 5, 85, 45, 16, 13, 35, 38, 41, 93, 85, 55, 29, 31, 80, 35, 8, 31, 60, 64, 100, 54, 5, 68, 44, 47, 20, 24, 96, 10, 24, 67, 7, 90, 96, 50, 30, 77, 83, 56, 19, 9, 40, 20, 37, 42, 24, 21, 91, 46, 1, 94, 7, 7, 28, 50, 72, 65, 13, 93, 87, 77, 38, 28, 37, 33, 45, 88, 5, 89, 55, 16, 99, 93, 6, 6, 56, 12, 88, 20, 21, 78, 30, 33, 100, 26, 31, 95, 16, 38, 13, 29, 46, 13, 75, 1, 29, 18, 56, 34, 20, 35, 59, 60, 81, 62, 65, 9, 61, 34, 10, 38, 11, 3, 42, 29, 33, 50]
assert s.maxProfit(test) == 197