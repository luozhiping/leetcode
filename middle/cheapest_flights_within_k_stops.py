# 787. K 站中转内最便宜的航班
# https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/

import sys
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        if not flights:
            return -1
        flight = [[] for _ in range(n)]
        for f in flights:
            flight[f[0]].append(f[1:])
        self.minPrice = sys.maxsize

        def dfs(next, price, geted={}):
            if len(geted) >= K + 1:
                return
            for f in flight[next]:
                if f[0] in geted or f[1] + price > self.minPrice:
                    continue
                if f[0] == dst:
                    self.minPrice = min(self.minPrice, f[1] + price)
                else:
                    g = dict(geted)
                    g[f[0]] = True
                    dfs(f[0], f[1] + price, g)


        for f in flight[src]:
            if f[0] == dst:
                self.minPrice = min(self.minPrice, f[1])
            else:
                dfs(f[0], f[1], {f[0]:True})
        return self.minPrice if self.minPrice != sys.maxsize else -1









s = Solution()
print(s.findCheapestPrice(3,  [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))


import random
n = random.randint(1, 100)
flights = []
for i in range(random.randint(0, n*(n-1)//2)):
    src = random.randint(0, n - 1)
    dst = random.randint(0, n - 1)
    while src == dst:
        dst = random.randint(0, n - 1)
    flights.append([src, dst, random.randint(1, 10000)])
k = random.randint(0, n-1)
src = random.randint(0, n-1)
d = random.randint(0, n-1)
while src == d:
    d = random.randint(0, n - 1)
print(n, flights, src, d, k)

print(s.findCheapestPrice(n, flights, src,d,k))
