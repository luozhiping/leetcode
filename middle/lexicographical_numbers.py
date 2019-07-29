# 386. 字典序排数
# https://leetcode-cn.com/problems/lexicographical-numbers/

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        def dfs(cur):
            for i in range(10):
                if cur+i <= n:
                    result.append(cur+i)
                    dfs((cur+i)*10)
                else:
                    break

        for i in range(1, 10):
            if i <= n:
                result.append(i)
                dfs(i*10)
            else:
                break
        return result

s = Solution()
assert s.lexicalOrder(13) == [1,10,11,12,13,2,3,4,5,6,7,8,9]
import time
begin = time.time()
s.lexicalOrder(5000000)
print(time.time()-begin)