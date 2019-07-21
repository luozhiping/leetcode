# 360. 有序转化数组
# https://leetcode-cn.com/problems/sort-transformed-array/

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def cal(x):
            return a * x * x + b * x + c
        result = []
        if a > 0:
            middle = b / (-2 * a)
            start = 0
            end = len(nums) - 1
            while start < end:
                if abs(nums[start] - middle) >= abs(nums[end] - middle):
                    result.insert(0, cal(nums[start]))
                    start += 1
                else:
                    result.insert(0, cal(nums[end]))
                    end -= 1
            result.insert(0, cal(nums[start]))
        elif a < 0:
            middle = b / (-2 * a)
            start = 0
            end = len(nums) - 1
            while start < end:
                if abs(nums[start] - middle) >= abs(nums[end] - middle):
                    result.append(cal(nums[start]))
                    # print('start', nums[start], nums[end], cal(nums[start]))

                    start += 1
                else:
                    result.append(cal(nums[end]))
                    # print('end', nums[start], nums[end], cal(nums[end]))

                    end -= 1
            result.append(cal(nums[start]))
        else:
            if b >= 0:
                return [cal(nums[i]) for i in range(0, len(nums))]
            elif b < 0:
                return [cal(nums[i]) for i in range(len(nums) - 1, -1, -1)]
        return result


s = Solution()
# assert s.sortTransformedArray([-4,-2,2,4], 1, 3, 5) == [3,9,15,33]
# assert s.sortTransformedArray([-4,-2,2,4], -1, 3, 5) == [-23,-5,1,7]

import random
test = []
for i in range(random.randint(1, 100)):
    test.append(random.randint(1, 100))

print(test)
test = [-100,-100,-89,-85,-82,-79,-75,-72,-69,-64,-62,-53,-41,-41,-40,-34,-28,-26,-26,-26,-25,-24,-19,-18,-11,-3,8,8,12,17,19,19,29,30,32,48,48,50,67,67,78,88,89,98]

assert s.sortTransformedArray(test, -96, -49, -35) == [-955135,-955135,-926821,-764812,-756090,-747771,-689470,-641521,-595300,-587921,-536360,-494171,-453710,-434262,-434262,-390115,-366021,-267102,-242485,-223571,-223571,-159402,-159402,-151675,-109345,-99907,-87905,-82192,-73927,-63657,-63657,-63657,-58810,-54155,-35622,-35622,-33760,-30257,-28612,-14447,-11112,-6571,-6571,-752]