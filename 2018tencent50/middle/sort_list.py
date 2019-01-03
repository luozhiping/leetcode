# 排序链表
# https://leetcode-cn.com/problems/sort-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        mid = self.getMid(head)
        if mid:
            second = mid.next
            mid.next = None
        return self.mergeList(self.sortList(head), self.sortList(second))

    def mergeList(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        ret = ListNode(-0)
        tmp = ret
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                tmp = tmp.next
                list1 = list1.next
            else:
                tmp.next = list2
                tmp = tmp.next
                list2 = list2.next
        if list1:
            tmp.next = list1
        elif list2:
            tmp.next = list2
        ret = ret.next
        return ret


    def getMid(self, head):
        if not head:
            return None
        if not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

node = ListNode(4)
node.next = ListNode(2)
node.next.next = ListNode(1)
node.next.next.next = ListNode(3)
# node.next.next.next.next = ListNode(5)

s = Solution()
r = s.sortList(node)
while r:
    print(r.val)
    r = r.next