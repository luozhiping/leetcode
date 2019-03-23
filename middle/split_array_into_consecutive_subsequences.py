# 659. 分割数组为连续子序列
# https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = {}
        need = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for num in nums:
            if freq[num] == 0:
                continue
            if num in need and need[num] > 0:
                need[num] -= 1
                if num+1 in need:
                    need[num + 1] += 1
                else:
                    need[num + 1] = 1
            elif num+1 in freq and num+2 in freq and freq[num+1]>0 and freq[num+2]>0:
                freq[num+1] -= 1
                freq[num+2] -= 1
                if num+3 in need:
                    need[num+3] += 1
                else:
                    need[num+3] = 1
            else:
                return False
            freq[num] -= 1
        return True
s = Solution()
print(s.isPossible([1,2,3,3,4,4,5,5]))