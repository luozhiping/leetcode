# 25. k个一组翻转链表
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        if k == 1:
            return head

        def beginReverse(lastHead, head, tail):
            lastHead.next = head
            current = head.next
            while current != tail:
                first = lastHead.next
                next = current.next
                #first.next = first.next.next
                lastHead.next = current
                current.next = first
                current = next

            first = lastHead.next
            head.next = current.next
            lastHead.next = current
            current.next = first
            return head

        h = head
        t = head.next
        step = 1
        lastHead = ListNode(-1)
        lastHead.next = head
        head = lastHead
        while t:
            if step < k - 1:
                step += 1
                t = t.next
            else:
                tmp = t
                nextH = t.next
                head = beginReverse(head, h, t)
                h = nextH
                if not h:
                    break
                t = h.next
                step = 1
        return lastHead.next

head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

s = Solution()
result = s.reverseKGroup(head, 5)
while result:
    print(result.val)
    result = result.next