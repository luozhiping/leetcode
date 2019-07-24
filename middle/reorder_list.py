# 143. 重排链表
# https://leetcode-cn.com/problems/reorder-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start = head
        end = head
        while end.next:
            end = end.next
            if end.next:
                start = start.next
                end = end.next
            else:
                break
        # print(start.val)

        lastHalf = start.next
        index = start.next
        start.next = None
        last = None
        next = None
        while index:
            if index.next:
                # next = index.next.next
                # index.next.next = index
                next = index.next
                index.next = last
                last = index
                index = next
            else:
                index.next = last
                lastHalf = index
                break

        # while lastHalf:
        #     print(lastHalf.val)
        #     lastHalf = lastHalf.next
        firstHalf = head
        while firstHalf and lastHalf:
            next = firstHalf.next
            firstHalf.next = lastHalf
            lNext = lastHalf.next
            lastHalf.next = next
            firstHalf = next
            lastHalf = lNext

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)



s = Solution()
print(s.reorderList(head))