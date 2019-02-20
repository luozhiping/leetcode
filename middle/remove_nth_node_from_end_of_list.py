# 19. 删除链表的倒数第N个节点
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        if head.next == None and n == 1:
            return None
        if head.next == None and n == 0:
            return head
        index1 = head
        index2 = head
        for i in range(n):
            index2 = index2.next

        if index2 == None:
            return head.next

        while index2.next != None:
            index1 = index1.next
            index2 = index2.next

        index1.next = index1.next.next
        return head


node = ListNode(1)
node.next = ListNode(2)
# node.next.next = ListNode(3)
# node.next.next.next = ListNode(4)
# node.next.next.next.next = ListNode(5)
s = Solution()
print(s.removeNthFromEnd(node, 2))