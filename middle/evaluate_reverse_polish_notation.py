# 150. 逆波兰表达式求值
# https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        stack = []
        valid = ["+", "-", "*", "/"]
        for token in tokens:
            if token in valid:
                num1 = stack.pop(-1)
                num2 = stack.pop(-1)
                if token == "+":
                    stack.append(num1+num2)
                elif token == "-":
                    stack.append(num2-num1)
                elif token == "*":
                    stack.append(num1*num2)
                else:
                    stack.append(int(num2/num1))
            else:
                if token.isnumeric():
                    stack.append(int(token))
                elif token[0] == "-" and token[1:].isnumeric():
                    stack.append(-int(token[1:]))
        # print(stack)
        return stack[0]


s = Solution()
assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
