# 147. 对链表进行插入排序
# https://leetcode-cn.com/problems/insertion-sort-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head
        root = ListNode(0)
        root.next = head

        current = [root]
        count = 0
        while cur:
            count += 1
            nextNode = cur.next
            added = False
            for i in range(1, len(current)):
                if cur.val < current[i].val:
                    current[i - 1].next = cur
                    cur.next = current[i]
                    current.insert(i, cur)
                    added = True
                    break
            if not added:
                current.append(cur)
            current[-1].next = nextNode
            cur = nextNode

            # print(value)

        return root.next
        # return root.next
        # return value[1:]
        # return root.next

s = Solution()
node = ListNode(4)
node.next = ListNode(2)
node.next.next = ListNode(1)
node.next.next.next = ListNode(3)
# print(s.insertionSortList(node))

import random
test = []
for i in range(random.randint(1, 100)):
    test.append(random.randint(1, 100))

print(test)
test = [88, 12, 70, 65, 80, 9, 80, 90, 66, 51, 92, 3, 64, 42, 49, 95, 71, 2, 66, 30, 78, 97, 80, 48, 82, 46, 71, 62, 5, 69, 75, 79, 55, 20, 28, 76, 47, 32, 33]
root = ListNode(test[0])
cur = root
for i in range(1, len(test)):
    cur.next = ListNode(test[i])
    cur = cur.next
# print(s.insertionSortList(root))
assert s.insertionSortList(root) == sorted(test)