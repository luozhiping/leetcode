# 799. 香槟塔
# https://leetcode-cn.com/problems/champagne-tower/

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        tower = [[poured]]
        for i in range(1, query_row+1):
            tmp = []
            last = tower[-1]
            tmp.append(max(0, (last[0]-1)/2))
            for j in range(len(last) - 1):
                left = max(0, (last[j]-1)/2)
                right = max(0, (last[j+1]-1)/2)
                tmp.append(left+right)
            tmp.append(max(0, (last[-1] - 1)/2))
            tower.append(tmp)
            print(tmp)
        return 1.0 if tower[query_row][query_glass] >= 1 else tower[query_row][query_glass]




s = Solution()
print(s.champagneTower(2, 1, 1))

import random
poured = random.randint(0, 10**6)
query_row = random.randint(90, 99)
query_glass = random.randint(20, 30)
print(poured, query_row, query_glass)
# print(s.champagneTower(642377764 ,
# 90 ,
# 71,
# ))
print(s.champagneTower(poured, query_row, query_glass))