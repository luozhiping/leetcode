# 445. 两数相加 II
# https://leetcode-cn.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        lastNode = None
        pos = False
        # length = max(len(l1), len(l2))
        while stack1 or stack2:
            cur = 0
            if stack1:
                cur += stack1.pop(-1)
            if stack2:
                cur += stack2.pop(-1)
            if pos:
                cur += 1
            if cur >= 10:
                pos = True
                cur -= 10
            else:
                pos = False
            node = ListNode(cur)
            node.next = lastNode
            lastNode = node
        if pos:
            node = ListNode(1)
            node.next = lastNode
            lastNode = node
        return lastNode



l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s = Solution()
result = s.addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next

import random
test1 = ListNode(random.randint(1, 9))
tmp = test1
tmp1 = [test1.val]
for i in range(random.randint(1, 50)):
    tmp.next = ListNode(random.randint(1, 9))
    tmp1.append(tmp.val)
    tmp = tmp.next

test2 = ListNode(random.randint(1, 9))
tmp = test2
tmp2 = [test2.val]
for i in range(random.randint(1, 50)):
    tmp.next = ListNode(random.randint(1, 9))
    tmp2.append(tmp.val)
    tmp = tmp.next

print(tmp1, tmp2)
result = s.addTwoNumbers(test1, test2)
while result:
    print(result.val)
    result = result.next
