# 环形链表
# https://leetcode-cn.com/problems/linked-list-cycle/


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True




link1 = ListNode(1)
link1.next = ListNode(2)
link1.next.next = ListNode(4)
link1.next.next.next = ListNode(5)
linke2 = link1.next.next.next
link1.next.next.next.next = ListNode(6)
link1.next.next.next.next.next = linke2

s = Solution()
print(s.hasCycle(link1))