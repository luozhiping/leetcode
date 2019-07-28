# 1135. 最低成本联通所有城市
# https://leetcode-cn.com/problems/connecting-cities-with-minimum-cost/

class Solution(object):
    def minimumCost(self, N, conections):
        """
        :type N: int
        :type conections: List[List[int]]
        :rtype: int
        """
        # print(N, len(conections))
        s = 0
        maps = sorted(conections, key=lambda x:x[2])
        parent = [-1 for i in range(N+1)]
        count = N
        def findParent(x):
            # print(x, parent[x])
            if parent[x] == -1:
                return x
            else:
                return findParent(parent[x])
        for e in maps:
            # print(p)
            p1 = findParent(e[0])
            p2 = findParent(e[1])
            if p1 != p2:
                if count == 1:
                    break
                parent[p1] = p2
                s += e[2]
                count -= 1
                # print(e, findParent(e[0]), findParent(e[1]), count)
        # print(s, count)
        if count > 1:
            return -1
        return s