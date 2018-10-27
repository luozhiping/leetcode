# 反转链表
# https://leetcode-cn.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        def do_reverse(root):
            if root.next:
                now, new_head = do_reverse(root.next)
                now.next = root
                now = now.next
                root.next = None
            else:
                return root, root
            return now, new_head
        return do_reverse(head)[1]


link1 = ListNode(1)
# link1.next = ListNode(2)
# link1.next.next = ListNode(4)
# link1.next.next.next = ListNode(5)
# link1.next.next.next.next = ListNode(6)
# link1.next.next.next.next.next = ListNode(7)

s = Solution()
new_head = s.reverseList(link1)

while new_head:
    print(new_head.val)
    new_head = new_head.next