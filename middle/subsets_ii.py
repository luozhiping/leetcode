# 90. 子集 II
# https://leetcode-cn.com/problems/subsets-ii/

class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums = sorted(nums)
        result = [[]]
        left = 0
        length = 0
        for i in range(len(nums)):
            num = nums[i]
            if i != 0 and nums[i] == nums[i - 1]:
                left = len(result) - length
            else:
                left = 0
            length = len(result) - 1
            for j in range(left, len(result)):
                re = list(result[j])
                re.append(num)
                result.append(re)
        return result

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums = sorted(nums)
        def getSubSets(nums, fatherList):
            result = [fatherList]
            if not nums:
                return result
            for i in range(len(nums)):
                if i == 0:
                    l = list(fatherList)
                    l.append(nums[i])
                    r = getSubSets(nums[i+1:], l)
                    if r:
                        result.extend(r)
                else:
                    if nums[i] == nums[i - 1]:
                        continue
                    else:
                        l = list(fatherList)
                        l.append(nums[i])
                        r = getSubSets(nums[i + 1:], l)
                        if r:
                            result.extend(r)
            return result

        result = [[]]
        for i in range(len(nums)):
            if i == 0:
                r = getSubSets(nums[i + 1:], [nums[i]])
                if r:
                    result.extend(r)
            else:
                if nums[i] == nums[i - 1]:
                    continue
                else:
                    r = getSubSets(nums[i + 1:], [nums[i]])
                    if r:
                        result.extend(r)
        return result


s = Solution()
print(s.subsetsWithDup(
[4,4,4,1,4]))
