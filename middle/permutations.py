# 46. 全排列
# https://leetcode-cn.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.result = []
        def bt(numList, index):
            if index == len(numList):
                # if numList in self.result:
                #     print("ininininini:", numList)
                self.result.append(numList)

                return
            for i in range(index, len(numList)):
                newList = list(numList)
                newList[index], newList[i] = newList[i], newList[index]
                bt(newList, index + 1)


        for i in range(len(nums)):
            numList = list(nums)
            numList[0], numList[i] = numList[i], numList[0]
            bt(numList, 1)
        # print(len(self.result))

        return self.result

s = Solution()
test = [1, 2, 3, 4, 5]
answer = 1
for i in range(len(test)):
    answer *= i+1
result = s.permute(test)
for i in range(len(result)):
    print(result[i] ,i)