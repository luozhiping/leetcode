# 1120. 子树的最大平均值
# https://leetcode-cn.com/problems/maximum-average-subtree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.result = 0
        def dfs(node):
            count_all = 1
            val_all = node.val
            if node.left:
                result, count = dfs(node.left)
                val_all += result * count
                count_all += count

            if node.right:
                result, count = dfs(node.right)
                val_all += result * count
                count_all += count
            cur_mean = val_all/float(count_all)
            self.result = max(self.result, cur_mean)
            return cur_mean, count_all


        dfs(root)
        return self.result

# node = TreeNode(5)
# node.left = TreeNode(6)
# node.left.left = TreeNode(5)
# node.right = TreeNode(1)
# node.right.left = TreeNode(5)
# node.right.right = TreeNode(3)
node = TreeNode(2)
node.right = TreeNode(1)

s = Solution()
print(s.maximumAverageSubtree(node))