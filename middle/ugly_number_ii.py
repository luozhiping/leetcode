# 264. 丑数 II
# https://leetcode-cn.com/problems/ugly-number-ii/

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        uglyList = [1]
        ugli2 = 0
        ugli3 = 0
        ugli5 = 0
        while len(uglyList) < n:
            uglyNext = min(uglyList[ugli2]*2, uglyList[ugli3]*3, uglyList[ugli5]*5)
            uglyList.append(uglyNext)
            while uglyList[ugli2]*2<=uglyNext:
                ugli2+=1
            while uglyList[ugli3]*3<=uglyNext:
                ugli3+=1
            while uglyList[ugli5]*5<=uglyNext:
                ugli5+=1
        return uglyList[-1]

s = Solution()
print(s.nthUglyNumber(1))