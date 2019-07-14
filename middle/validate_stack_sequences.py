# 946. 验证栈序列
# https://leetcode-cn.com/problems/validate-stack-sequences/

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not pushed or not popped:
            return True
        # push = pushed.pop(0)

        # pop = popped.pop(0)

        stack = [pushed.pop(0)]

        while pushed and popped:
            if stack and stack[-1] == popped[0]:
                stack.pop(-1)
                popped.pop(0)
            else:
                stack.append(pushed.pop(0))
        if popped:
            while popped:
                if stack[-1] == popped[0]:
                    stack.pop(-1)
                    popped.pop(0)
                else:
                    return False
        return True


s = Solution()
print(s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))