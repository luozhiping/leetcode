# 322. 零钱兑换
# https://leetcode-cn.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0 or not coins:
            return 0
        counts = [amount+1] * (amount + 1)
        coins = sorted(coins)

        for i in range(1, len(counts)):
            for j in range(len(coins)):
                if i - coins[j] == 0:
                    counts[i] = 1
                elif i - coins[j] < 0:
                    continue
                else:
                    counts[i] = min(counts[i], counts[i - coins[j]] + 1)
        return counts[amount] if counts[amount] <= amount else -1

s = Solution()
print(s.coinChange([2147483647],
2))