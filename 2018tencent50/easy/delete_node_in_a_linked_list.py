# 删除链表中得节点
# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

link2 = ListNode(2)
link2.next = ListNode(0)
link2.next.next = ListNode(1)
link2.next.next.next = ListNode(3)
# link2.next.next.next.next = ListNode(9)

s = Solution()
s.deleteNode(link2.next)


while link2:
    print(link2.val)
    link2 = link2.next