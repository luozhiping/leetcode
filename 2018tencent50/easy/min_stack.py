# 最小栈
# https://leetcode-cn.com/problems/min-stack/


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            x = self.stack.pop()
            if self.min_stack and self.min_stack[-1] == x:
                self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1] if self.min_stack else None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(4)
obj.push(3)
obj.push(3)

obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)

# print([].pop())