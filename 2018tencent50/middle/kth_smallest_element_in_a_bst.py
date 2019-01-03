# 二叉搜索树中第K小的元素
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        result = self.dfs(root)
        return result[k-1]

    def dfs(self, root):
        tmp = list()
        if root.left:
            tmp.extend(self.dfs(root.left))
        tmp.append(root.val)
        if root.right:
            tmp.extend(self.dfs(root.right))
        return tmp

t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(6)
t.left.left = TreeNode(2)
t.left.left.left = TreeNode(1)
t.left.right = TreeNode(4)

s = Solution()
print(s.kthSmallest(t, 3))