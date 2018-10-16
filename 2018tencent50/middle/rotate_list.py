# 旋转链表
# https://leetcode-cn.com/problems/rotate-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        if not head or not head.next or k == 0:
            return head
        count = 1
        while node.next is not None:
            node = node.next
            count += 1
        node.next = head
        k = count - k % count
        for i in range(k):
            node = node.next
        result = node.next
        node.next = None
        return result



node = ListNode(1)
node.next = ListNode(2)
# node.next.next = ListNode(3)
# node.next.next.next = ListNode(4)
# node.next.next.next.next = ListNode(5)
s = Solution()
print(s.rotateRight(node, 2))