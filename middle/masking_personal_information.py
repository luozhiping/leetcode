# 831. 隐藏个人信息
# https://leetcode-cn.com/problems/masking-personal-information/

class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if "@" in S:
            S = S.lower()
            S = S[0] + "*****" + S[S.index("@")-1:]
            return S
        nums = []
        for c in S:
            if c.isnumeric():
                nums.append(c)
        result = []
        if len(nums) > 10:
            result.append("+")
            result.append(len(nums[:-10])*"*")
            result.append("-")
        result.extend("***-***-")
        result.extend(nums[-4:])
        # print(result)
        return "".join(result)

s = Solution()
assert s.maskPII("LeetCode@LeetCode.com") == "l*****e@leetcode.com"
assert s.maskPII("AB@qq.com") == "a*****b@qq.com"
assert s.maskPII("1(234)567-890") == "***-***-7890"
assert s.maskPII("86-(10)12345678") == "+**-***-***-5678"

