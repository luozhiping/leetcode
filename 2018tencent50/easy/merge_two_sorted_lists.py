# 合并两个有序列表
# https://leetcode-cn.com/problems/merge-two-sorted-lists/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        now = result
        while l1 and l2:
            if l1.val <= l2.val:
                now.next = l1
                now = now.next
                l1 = l1.next
            else:
                now.next = l2
                now = now.next
                l2 = l2.next
        if l1:
            now.next = l1
        else:
            now.next = l2
        return result.next


link1 = ListNode(1)
link1.next = ListNode(2)
link1.next.next = ListNode(4)

link2 = ListNode(1)
link2.next = ListNode(3)
link2.next.next = ListNode(4)
link2.next.next.next = ListNode(9)
link2.next.next.next.next = ListNode(9)

s = Solution()
result = s.mergeTwoLists(link1, link2)

while result:
    print(result.val)
    result = result.next