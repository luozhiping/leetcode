# 98. 验证二叉搜索树
# https://leetcode-cn.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        def bianli(node):
            if node.left:
                if not bianli(node.left):
                    return False
            if result and result[-1] >= node.val:
                return False
            result.append(node.val)
            if node.right:
                if not bianli(node.right):
                    return False
            return True

        if not root:
            return True

        if root.left:
            if not bianli(root.left):
                return False
        if result and result[-1] >= root.val:
                return False
        result.append(root.val)
        if root.right:
            if not bianli(root.right):
                return False

        return True



root = TreeNode(1)
root.left = TreeNode(1)
# root.right = TreeNode(15)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(20)
s = Solution()
print(s.isValidBST(root))