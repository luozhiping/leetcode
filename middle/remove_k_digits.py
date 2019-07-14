# 402. 移掉K位数字
# https://leetcode-cn.com/problems/remove-k-digits/

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <= k:
            return "0"
        end = len(num) - k
        count = 0
        # print(end, num[end])
        start = 0
        result = ""
        while count < end:
            minValue = num[start]
            minIndex = start
            for i in range(start + 1, k + count + 1):
                if num[i] < minValue:
                    minValue = num[i]
                    minIndex = i
            result += num[minIndex]
            # k -= 1
            start = minIndex+1
            count += 1
            # end = len(num) - k
        # result.append(num[start:])
        return "0" if len(result) == 0 else str(int(result))

s = Solution()
print(s.removeKdigits("1432219", 3))
print(s.removeKdigits("10200", 1))
print(s.removeKdigits("10", 2))