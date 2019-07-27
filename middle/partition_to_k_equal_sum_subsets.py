# 698. 划分为k个相等的子集
# https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums and not k:
            return False
        count = sum(nums)
        if count % k != 0:
            return False
        every = count // k
        flag = [False for _ in range(len(nums))]
        def cal(k, start, curSum):
            if k == 1:
                return True
            if curSum > every:
                return False
            if curSum == every:
                return cal(k-1, 0, 0)
            for i in range(start, len(nums)):
                if flag[i]:
                    continue
                flag[i] = True
                if cal(k, i+1, curSum+nums[i]):
                    return True
                flag[i] = False
            return False




        return cal(k, 0, 0)

s = Solution()
# print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))

# assert s.canPartitionKSubsets([10,10,10,7,7,7,7,7,7,6,6,6], 3) == True
assert s.canPartitionKSubsets([2,2,2,2,3,4,5]
,4) == False