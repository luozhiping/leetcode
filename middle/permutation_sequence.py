# 60. 第k个排列
# https://leetcode-cn.com/problems/permutation-sequence/

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i+1 for i in range(n)]
        self.result = None
        def bt(numList, index, k):
            numList = numList[:index] + sorted(numList[index:])
            if index == len(numList):
                # if numList in self.result:
                #     print("ininininini:", numList)
                # self.result.append(numList)
                if k == 1:
                    # print(numList, k)
                    self.result = numList
                return
            count = 1
            for i in range(len(nums) - (index + 1), 0, -1):
                count *= i
            for i in range(index, len(numList)):
                if count < k:
                    k -= count
                    continue
                newList = list(numList)
                newList[index], newList[i] = newList[i], newList[index]
                bt(newList, index + 1, k)
                break


        count = 1
        for i in range(2, len(nums)):
            count *= i
        for i in range(len(nums)):
            if count < k:
                k -= count
                continue
            numList = list(nums)
            numList[0], numList[i] = numList[i], numList[0]
            bt(numList, 1, k)
            break
        return "".join(map(str, self.result))

s = Solution()
print(s.getPermutation(5, 12))
#
# [1, 2, 3, 4, 5] 0
# [1, 2, 3, 5, 4] 1
# [1, 2, 4, 3, 5] 2
# [1, 2, 4, 5, 3] 3
# [1, 2, 5, 4, 3] 4
# [1, 2, 5, 3, 4] 5
# [1, 3, 2, 4, 5] 6
# [1, 3, 2, 5, 4] 7
# [1, 3, 4, 2, 5] 8
# [1, 3, 4, 5, 2] 9
# [1, 3, 5, 4, 2] 10
# [1, 3, 5, 2, 4] 11
# [1, 4, 3, 2, 5] 12
# [1, 4, 3, 5, 2] 13