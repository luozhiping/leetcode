# 1130. 叶值的最小代价生成树
# https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/

import sys
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        leftMin = {}
        rightMin = {}

        self.board = [[0 for _ in range(len(arr))] for _ in range(len(arr))]

        def calNext(array, start, end):
            if len(array) == 2:
                return array[0] * array[1]
            if len(array) == 1:
                return 0
            minResut = sys.maxsize
            for i in range(1, len(array)):
                left = array[:i]
                right = array[i:]
                result = sorted(left)[-1] * sorted(right)[-1]
                leftResult = 0
                rightResult = 0
                if i != 1:
                    if self.board[start][start + i-1] != 0:
                        leftResult = self.board[start][start + i-1]
                    else:
                        leftResult = calNext(left, start, start+i-1)
                        self.board[start][start + i-1] = leftResult
                if i != len(array) - 1:
                    if self.board[start+i][end] != 0:
                        rightResult = self.board[start+i][end]
                    else:
                        rightResult = calNext(right, start+i, end)
                        self.board[start + i][end] = rightResult
                result = result + leftResult + rightResult
                minResut = min(result, minResut)
            return minResut


        result = calNext(arr, 0, len(arr) - 1)
        return result

s = Solution()
# assert s.mctFromLeafValues([15,13,5,3,15]) == 500
assert s.mctFromLeafValues([1,11,8,8,13,2,6,1,7,6,8,10,14,9,13,15,11,2,13,15]) == 5