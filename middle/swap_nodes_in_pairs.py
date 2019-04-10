# 24. 两两交换链表中的节点
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        index1 = head
        index2 = head.next
        fakeHead = ListNode(-1)
        fakeHead.next = head
        resultHead = fakeHead
        while index2:
            tmp = index2.next
            fakeHead.next = index2
            index2.next = index1
            index1.next = tmp
            fakeHead = index1
            index1 = tmp
            if index1:
                index2 = index1.next
            else:
                index2 = None
        return resultHead.next

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)


s = Solution()
node = s.swapPairs(root)
while node:
    print(node.val)
    node = node.next