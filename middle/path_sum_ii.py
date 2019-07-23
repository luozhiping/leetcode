# 113. 路径总和 II
# https://leetcode-cn.com/problems/path-sum-ii/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        tmp = {}
        def dfs(node, sum1, curList):
            if sum1 == 0 and not node.left and not node.right:
                result.append(curList)
                return
            if node.left:
                l = list(curList)
                l.append(node.left.val)
                dfs(node.left, sum1 - node.left.val, l)
            if node.right:
                l = list(curList)
                l.append(node.right.val)
                dfs(node.right, sum1 - node.right.val, l)

        if root:
            dfs(root, sum - root.val, [root.val])
        return result


node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(8)

node.left.left = TreeNode(11)
node.right.left = TreeNode(13)
node.right.right = TreeNode(4)
node.right.right.left = TreeNode(5)
node.right.right.right = TreeNode(1)
node.left.left.left = TreeNode(7)
node.left.left.right = TreeNode(2)


s = Solution()
print(s.pathSum(node, 9))