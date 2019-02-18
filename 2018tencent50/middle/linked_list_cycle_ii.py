# 环形列表 II
# https://leetcode-cn.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        p = head
        p2 = head
        cycle = False
        while p.next != None and p2.next != None and p2.next.next != None:
            p = p.next
            p2 = p2.next.next
            if p == p2:
                cycle = True
                break
        if cycle:
            q = head
            while p != q:
                p = p.next
                q = q.next
            return q
        return None



node = ListNode(3)
node.next = ListNode(2)
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)
# node.next.next.next.next = node.next
s = Solution()
print(s.detectCycle(node))