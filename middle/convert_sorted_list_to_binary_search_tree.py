# 109. 有序链表转换二叉搜索树
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        seq = []
        while head:
            seq.append(head.val)
            head = head.next

        def buildTree(left, node, right):
            if left:
                mid = len(left) // 2
                node.left = TreeNode(left[mid])
                buildTree(left[:mid], node.left, left[mid+1:])
            if right:
                mid = len(right) // 2
                node.right = TreeNode(right[mid])
                buildTree(right[:mid], node.right, right[mid + 1:])



        mid = len(seq) // 2
        root = TreeNode(seq[mid])
        buildTree(seq[:mid], root, seq[mid+1:])
        return root


link = ListNode(-10)
link.next = ListNode(-3)
link.next.next = ListNode(0)
link.next.next.next = ListNode(5)
link.next.next.next = ListNode(9)

s = Solution()
root = s.sortedListToBST(link)
print(root.val)