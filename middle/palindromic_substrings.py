# 647. 回文子串
# https://leetcode-cn.com/problems/palindromic-substrings/

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        board = [[0 for _ in range(len(s))] for _ in range(len(s))]
        result = 0
        for j in range(len(s)):
            for i in range(len(s)):
                if i > j:
                    continue
                elif i == j:
                    result += 1
                    board[i][j] = 1
                elif j - 1 == i and s[i] == s[j]:
                    result += 1
                    board[i][j] = 1
                elif s[i] == s[j] and i + 1 < len(s) and j - 1 >= 0 and board[i][j] == 0:
                    board[i][j] = board[i+1][j-1]
                    if board[i][j] == 1:
                        result += 1

        # print(board)
        return result
s = Solution()
print(s.countSubstrings("abc"))