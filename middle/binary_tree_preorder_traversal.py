# 144. 二叉树的前序遍历
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        result.append(root.val)
        if root.left:
            result.extend(self.preorderTraversal(root.left))
        if root.right:
            result.extend(self.preorderTraversal(root.right))
        return result



root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

s = Solution()
print(s.preorderTraversal(root))