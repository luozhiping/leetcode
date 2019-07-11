# 227. 基本计算器 II
# https://leetcode-cn.com/problems/basic-calculator-ii/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        tmp = s.split("+")
        result = 0
        for str in tmp:
            t = str.split("-")
            re = None
            for str2 in t:
                stack = []

                mid = 0
                for c in str2:
                    if c.isnumeric():
                        mid = mid * 10 + int(c)
                    else:
                        if stack:
                            if stack[-1] == '*':
                                stack.pop(-1)
                                stack.append(mid * stack.pop(-1))
                            elif stack[-1] == '/':
                                stack.pop(-1)
                                stack.append(stack.pop(-1) // mid)
                        else:
                            stack.append(mid)
                        mid = 0
                        stack.append(c)
                if not stack:
                    stack.append(mid)
                else:
                    if stack[-1] == '*':
                        stack.pop(-1)
                        stack.append(mid * stack.pop(-1))
                    elif stack[-1] == '/':
                        stack.pop(-1)
                        stack.append(stack.pop(-1) // mid)
                # print(stack)
                if re is None:
                    re = stack[-1]
                else:
                    re -= stack[-1]
                # print(re)
            if re is not None:
                result += re
        return result

s = Solution()
print(s.calculate("0-2147483647"))