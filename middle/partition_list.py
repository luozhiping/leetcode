# 86. 分隔链表
# https://leetcode-cn.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fakeHead1 = ListNode(-1)
        cur1 = fakeHead1
        fakeHead2 = ListNode(-2)
        cur2 = fakeHead2
        while head:
            if head.val < x:
                cur1.next = head
                cur1 = head
            else:
                cur2.next = head
                cur2 = head
            head = head.next
        cur1.next = fakeHead2.next
        cur2.next = None
        return fakeHead1.next

root = ListNode(1)
root.next = ListNode(4)
root.next.next = ListNode(3)
root.next.next.next = ListNode(2)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(2)

s = Solution()
node = s.partition(root,3 )
while node:
    print(node.val)
    node = node.next