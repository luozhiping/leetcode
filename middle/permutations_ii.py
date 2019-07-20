# 47. 全排列 II
# https://leetcode-cn.com/problems/permutations-ii/


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums = sorted(nums)
        self.result = []
        def bt(numList, index):
            numList = numList[:index] + sorted(numList[index:])
            if index == len(numList):
                # if numList in self.result:
                #     print("ininininini:", numList)
                self.result.append(numList)

                return
            for i in range(index, len(numList)):
                if i != index and numList[i] == numList[i-1]:
                    continue
                newList = list(numList)
                newList[index], newList[i] = newList[i], newList[index]
                bt(newList, index + 1)


        for i in range(len(nums)):
            if i != 0 and nums[i-1] == numList[i]:
                continue
            numList = list(nums)

            numList[0], numList[i] = numList[i], numList[0]

            bt(numList, 1)
        # print(len(self.result))

        return self.result



s = Solution()
# print(s.permuteUnique([2,2,1,1]))
r=s.permuteUnique([0,1,0,0,9])
for i in range(len(r)):
    print(r[i])

result= [[0,0,0,1,9],[0,0,0,9,1],[0,0,1,0,9],[0,0,1,9,0],[0,0,9,0,1],[0,0,9,1,0],[0,1,0,0,9],[0,1,0,9,0],[0,1,9,0,0],[0,9,0,0,1],[0,9,0,1,0],[0,9,1,0,0],[1,0,0,0,9],[1,0,0,9,0],[1,0,9,0,0],[1,9,0,0,0],[9,0,0,0,1],[9,0,0,1,0],[9,0,1,0,0],[9,1,0,0,0]]