# 638. 大礼包
# https://leetcode-cn.com/problems/shopping-offers/

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        dp = {}  # 初始化，dp,用于保存每个状态的最优解

        def dfs(cur):
            val = sum(cur[i] * price[i] for i in range(len(needs)))  # 不用礼包时的价格
            for spec in special:
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0:  # 过滤掉，礼包里面的商品多于需求的，礼包， 其中这个一步也相当于减枝
                    val = min(val, dp.get(tuple(tmp), dfs(tmp)) + spec[-1])  # 循环--递归--获取最优解
            dp[tuple(cur)] = val
            return val

        return dfs(needs)


s = Solution()
print(s.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))