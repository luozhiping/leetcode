# 718. 最长重复子数组
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0
        result = 0
        board = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    board[i][j] = board[i-1][j-1] + 1
                    result = max(result, board[i][j])
                else:
                    continue
        return result


s = Solution()
print(s.findLength([1,3], [1,2]))