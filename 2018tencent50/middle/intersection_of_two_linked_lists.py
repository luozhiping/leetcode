# 相交链表
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        countA = 1
        countB = 1

        node = headA
        while node.next:
            node = node.next
            countA += 1
        nodeA = node

        node = headB
        while node.next:
            node = node.next
            countB += 1

        if node != nodeA:
            return None

        if countA > countB:
            for i in range(countA - countB):
                headA = headA.next
        else:
            for i in range(countB - countA):
                headB = headB.next
        while headA is not None:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next


link1 = ListNode("a1")
link1.next = ListNode("a2")
link1.next.next = ListNode("c1")
link1.next.next.next = ListNode("c2")
link1.next.next.next.next = ListNode("c3")


link2 = ListNode("b1")
link2.next = ListNode("b2")
link2.next.next = ListNode("b3")
link2.next.next.next = link1.next.next

s = Solution()
print(s.getIntersectionNode(link1, link2))
