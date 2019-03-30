# 494. 目标和
# https://leetcode-cn.com/problems/target-sum/
class Solution2(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        rest = 0
        zero = 0
        new_nums = []
        for num in nums:
            if num == 0:
                zero += 1
            else:
                new_nums.append(num)
            rest += num

        index = 0
        result = 0
        if new_nums:
            summon = [new_nums[0], -new_nums[0]]
            while index < len(new_nums):
                rest = rest - new_nums[index]
                seq = []
                while summon:
                    cur = summon.pop(0)
                    tmp = S - cur
                    if rest == abs(tmp):
                        result += 1
                        continue

                    if rest < abs(tmp):
                        continue
                    seq.append(cur + new_nums[index+1])
                    seq.append(cur - new_nums[index+1])
                summon.extend(seq)
                index += 1
        elif rest == abs(S):
            result = 1
        return result * 2 ** zero


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        summon = sum(nums)
        if S > summon or (summon + S) % 2 == 1:
            return 0

        summon = (summon + S) // 2
        dp = [0 for _ in range(summon+2)]
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(summon, nums[i]-1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[summon]




s = Solution()
print(s.findTargetSumWays([42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47],
38))