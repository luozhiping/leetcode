# 92. 反转链表 II
# https://leetcode-cn.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: inta
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        prev = None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

            # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head




root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)

s = Solution()
n = s.reverseBetween(root, 2, 4)
while n:
    print(n.val)
    n = n.next