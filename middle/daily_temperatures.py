# 739. 每日温度
# https://leetcode-cn.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []
        result = [0 for _ in range(len(T))]
        for i in range(len(T) - 2, -1, -1):
            index = i + 1
            while index < len(T):
                if T[index] > T[i]:
                    result[i] = index - i
                    break
                else:
                    if result[index] != 0:
                        index += result[index]
                    else:
                        break
        return result


s = Solution()
print(s.dailyTemperatures([2, 1]))