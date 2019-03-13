# 82. 删除排序链表中的重复元素 II
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        origin = ListNode(-1)
        last = origin
        last.next = head
        cur = head
        next = cur.next

        current = cur.val
        while next:
            if next.val == current:
                next = next.next
                last.next = next
                while next:
                    if next.val == current:
                        next = next.next
                        last.next = next
                    else:
                        last.next = next
                        cur = next
                        current = cur.val
                        next = next.next
                        break
            else:
                last = cur
                cur = next
                current = cur.val
                next = next.next
        return origin.next




head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(8)

s = Solution()

node = s.deleteDuplicates(head)
while node:
    print(node.val)
    node = node.next

