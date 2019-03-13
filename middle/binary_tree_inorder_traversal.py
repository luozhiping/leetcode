# 94. 二叉树的中序遍历
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        result = []

        while root:

            stack.append(root)
            if root.left:
                root = root.left
            else:
                tail = stack.pop(-1)
                result.append(tail.val)
                if tail.right:
                    root = tail.right
                    continue
                while tail and not tail.right and len(stack) > 0:
                    tail = stack.pop(-1)
                    result.append(tail.val)
                if tail:
                    root = tail.right
                else:
                    break
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

s = Solution()
print(s.inorderTraversal(root))