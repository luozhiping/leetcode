# 有效的括号
# https://leetcode-cn.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack1 = []
        left_parentheses = ["(","[","{"]
        right_parentheses = {")":"(","]":"[","}":"{"}

        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in left_parentheses:
                stack1.append(i)
            else:
                if stack1 and stack1.pop() == right_parentheses[i]:
                    continue
                else:
                    return False
        return not stack1



s = Solution()
print(s.isValid("{[]}"))
print(s.isValid("()[]{})"))