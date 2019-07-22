# 921. 使括号有效的最少添加
# https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid/

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stackLeft = 0
        stackRight = 0
        for c in S:
            if c == "(":
                stackLeft += 1
            else:
                if stackLeft > 0:
                    stackLeft -=1
                else:
                    stackRight += 1
        return stackLeft + stackRight

s = Solution()
assert s.minAddToMakeValid("())") == 1
assert s.minAddToMakeValid("(((") == 3
assert s.minAddToMakeValid("()") == 0
assert s.minAddToMakeValid("()))((") == 4

import random
test = ""
for i in range(random.randint(500, 1000)):
    test +="(" if random.random()>=0.5 else ")"
print(test)
print(s.minAddToMakeValid(test))
