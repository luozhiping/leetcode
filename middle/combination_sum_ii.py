# 40. 组合总和 II
# https://leetcode-cn.com/problems/combination-sum-ii/

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates = sorted(candidates)
        result = []

        def bp(restCandidates, rest, tmp):
            if not restCandidates:
                return False
            for i in range(len(restCandidates)):

                if i > 0 and restCandidates[i] == restCandidates[i-1]:
                    continue
                n_rest = rest - restCandidates[i]
                # print("rest:", restCandidates, n_rest)

                if n_rest == 0:
                    tmp.append(restCandidates[i])
                    result.append(tmp)
                    return False
                elif n_rest > 0:
                    nt = list(tmp)
                    nt.append(restCandidates[i])

                    bp(restCandidates[i+1:], n_rest, nt)
                        # return False
                else:
                    # print(n_rest, restCandidates[i])
                    return False

        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            rest = target - candidates[i]
            tmp = [candidates[i]]
            # print(i, candidates[i], rest)
            if rest == 0:
                result.append(tmp)
                break
            if rest < 0:
                break
            bp(candidates[i+1:], rest, tmp)
        return result
s = Solution()
# print(s.combinationSum2([10,1,2,7,6,1,5], 8))

import random
test = []
for i in range(random.randint(1, 100)):
    test.append(random.randint(1, 100))
test_targe = random.randint(1, 100)
print(test, test_targe)
# test = [37, 66, 97, 32, 55, 39, 86, 64, 43, 91, 79, 27, 14, 43, 7, 42, 99, 70, 72, 19, 52, 31, 3, 59, 89, 20, 69, 62, 49, 47, 90, 81, 83, 87, 33, 66, 81, 75, 47, 25, 83, 37, 91, 14, 99, 12, 63, 79, 12, 93, 49, 81, 29, 56, 92, 27, 60, 14, 27, 23, 88, 14, 57, 93, 57, 67, 85, 14, 99, 9, 10, 37, 95, 49, 11, 11, 38, 31, 66, 33, 32, 35, 34, 30, 15, 68]
# test_targe = 76
print(len(s.combinationSum2(test, test_targe)))