# 129. 求根到叶子节点数字之和
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def dfs(node, lastSum):
            if not node.left and not node.right:
                self.result += lastSum
                return
            if node.left:
                dfs(node.left, lastSum*10+node.left.val)
            if node.right:
                dfs(node.right, lastSum*10+node.right.val)




        if root:
            dfs(root, root.val)


        return self.result



root = TreeNode(4)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

root.right = TreeNode(0)


s = Solution()
print(s.sumNumbers(root))
