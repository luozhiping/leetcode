# 39. 组合总和
# https://leetcode-cn.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates = sorted(candidates)
        def findCombination(seq, lastSum, index):
            if lastSum == target:
                return [seq]
            result = []
            for i in range(index, len(candidates)):
                num = candidates[i]
                l = list(seq)
                l.append(num)
                if lastSum + num == target:
                    result.append(l)
                elif lastSum + num > target:
                    break
                else:
                    result.extend(findCombination(l, lastSum + num, i))
            return result

        result = []
        for i in range(len(candidates)):
            num = candidates[i]
            result.extend(findCombination([num], num, i))
        return result



s = Solution()
print(s.combinationSum([8, 7, 4, 3], 11))