# 328. 奇偶链表
# https://leetcode-cn.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        nodeOdd = head
        nodeEven = head.next

        nodeOddHead = nodeOdd
        nodeEvenHead = nodeEven

        if nodeEven:
            current = nodeEven.next
            odd = True
            while current:
                if odd:
                    nodeOdd.next = current
                    nodeOdd = nodeOdd.next
                else:
                    nodeEven.next = current
                    nodeEven = nodeEven.next

                current = current.next
                odd = not odd
            nodeOdd.next = nodeEvenHead
            nodeEven.next = None
        return nodeOddHead



node = ListNode(2)
node.next = ListNode(1)
node.next.next = ListNode(3)
node.next.next.next = ListNode(5)
node.next.next.next.next = ListNode(6)
node.next.next.next.next.next = ListNode(4)
node.next.next.next.next.next.next = ListNode(7)


s = Solution()
node = s.oddEvenList(node)
while node:
    print(node.val)
    node = node.next