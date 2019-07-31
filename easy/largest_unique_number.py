# 1133. 最大唯一数
# https://leetcode-cn.com/problems/largest-unique-number/

class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return -1
        set = {}
        for num in A:
            set[num] = set.get(num, 0) + 1
        result = -1
        for key in set:
            if set[key] == 1:
                result = max(result, key)
        return result


s = Solution()
assert s.largestUniqueNumber([5,7,3,9,4,9,8,3,1]) == 8
assert s.largestUniqueNumber([9,9,8,8]) == -1