# 114. 二叉树展开为链表
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None

            cur = cur.right



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(8)
root.right.right = TreeNode(6)
root.right.left = TreeNode(7)


s = Solution()
print(s.flatten(root))
a = root
while a:
    print(a.val)
    a = a.right