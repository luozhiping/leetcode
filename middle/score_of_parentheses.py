# 856. 括号的分数
# https://leetcode-cn.com/problems/score-of-parentheses/

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        result = 0
        S = S.replace("()", "1")

        for c in S:
            if c == "(":
                stack.append(result)
                result = 0
            elif c == ")":
                result = result * 2 + stack.pop(-1)
            elif c == "1":
                result += 1
        # print(result)
        return result

s = Solution()
# assert s.scoreOfParentheses("()") == 1
# assert s.scoreOfParentheses("(())") == 2
# assert s.scoreOfParentheses("()()") == 2
assert s.scoreOfParentheses("(()(()))") == 6