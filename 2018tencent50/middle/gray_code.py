# 格雷编码
# https://leetcode-cn.com/problems/gray-code/

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        tmp = [0, 1]
        if n == 1:
            return tmp
        result = []
        final_result = []
        for _ in range(n - 1):
            result = []
            for index, i in enumerate(tmp):
                if index % 2 == 0:
                    result.append((i << 1) + 0)
                    result.append((i << 1) + 1)
                else:
                    result.append((i << 1) + 1)
                    result.append((i << 1) + 0)
            final_result = result
            tmp = result
        return final_result


s = Solution()
print(s.grayCode(1))

# print(0 << 1 + 1)
