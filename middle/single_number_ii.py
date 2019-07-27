# 137. 只出现一次的数字 II
# https://leetcode-cn.com/problems/single-number-ii/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = [0 for _ in range(32)]
        for num in nums:
            # num = abs(num)
            for i in range(32):
                times[i]+= num & 0x01
                num = num >> 1
                if not num:
                    break
        # print(times)
        result = 0
        if times[-1] % 3 > 0:
            for i in range(31, -1, -1):
                result = result << 1
                result += (times[i] % 3)^0x01
            result += 1
            # print(result)
            return -result
        else:
            for i in range(31, -1, -1):
                result = result << 1
                result += times[i] % 3
        # print(result)
        # print(result)
        return result

s= Solution()
assert s.singleNumber([2,2,3,2]) == 3
assert s.singleNumber([0,1,0,1,0,1,99]) == 99

assert s.singleNumber([-2,-2,1,1,-3,1,-3,-3,4,-2]) == 4