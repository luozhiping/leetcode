# 384. 打乱数组
# https://leetcode-cn.com/problems/shuffle-an-array/

import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ori = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.ori

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        tmp = list(self.ori)
        random.shuffle(tmp)
        return tmp



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()

s = Solution([1, 2, 3])
print(s.shuffle())
print(s.reset())