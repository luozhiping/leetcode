# 二叉树的最大深度
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 1 if root else 0
        left_depth = 0
        right_depth = 0
        # if root.left:
        left_depth += self.maxDepth(root.left)
        # if root.right:
        right_depth += self.maxDepth(root.right)

        return depth + max(left_depth,right_depth)


root = TreeNode(3)
root.left = TreeNode(9)
right = TreeNode(20)
root.right = right
right.left = TreeNode(15)
right.right = TreeNode(7)
right.left.left = TreeNode(15)

s = Solution()
print(s.maxDepth(root))
