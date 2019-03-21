# 179. 最大数
# https://leetcode-cn.com/problems/largest-number/

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ""
        def greaterThan(num1, num2):
            return int("%d%d" % (num1, num2)) > int("%d%d" % (num2, num1))

        def partition(nums, start, end):
            s = start
            e = end
            if start >= end:
                return
            base = nums[start]
            des = True
            while start < end:
                if des:
                    if not greaterThan(base, nums[end]):
                        nums[start] = nums[end]
                        des = False
                        start += 1
                    else:
                        end -=1
                else:
                    if greaterThan(base, nums[start]):
                        nums[end] = nums[start]
                        des = True
                        end -= 1
                    else:
                        start += 1
            nums[start] = base
            # print('partition:', nums, s, e, start)
            partition(nums, s, start - 1)
            partition(nums, start + 1, e)

        start = 0
        end = len(nums) - 1
        partition(nums, start, end)
        if nums[0] == 0:
            return "0"
        return "".join(map(str, nums))



s = Solution()
print(s.largestNumber([0, 0]))