# 22. 括号生成
# https://leetcode-cn.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(left, right, out=""):
            result = []
            if left < 0 or right < 0 or left > right:
                return result
            if left == 0 and right == 0:
                result.append(out)
                return result
            result.extend(generate(left - 1, right, out + "("))
            result.extend(generate(left, right - 1, out + ")"))
            return result

        result = []
        result.extend(generate(n, n, ""))

        return result

s = Solution()
print(s.generateParenthesis(3))