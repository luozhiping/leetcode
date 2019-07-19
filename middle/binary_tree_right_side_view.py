# 199. 二叉树的右视图
# https://leetcode-cn.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.currentMaxDepth = 0
        def search(node, currentDepth, rightDepth):
            rightDepth = 0
            leftDepth = 0
            if node.right:
                if currentDepth >= self.currentMaxDepth:
                    self.currentMaxDepth += 1
                    result.append(node.right.val)
                rightDepth = search(node.right, currentDepth + 1,0)
                # print(node.val, currentDepth, rightDepth)
            if node.left:
                if currentDepth >= self.currentMaxDepth:
                    self.currentMaxDepth += 1
                    result.append(node.left.val)
                leftDepth = search(node.left, currentDepth + 1,0)

                # print(node.val, currentDepth, leftDepth)

            return max(rightDepth, leftDepth)

        if root:
            result.append(root.val)
            search(root, 0, 0)

        return result




root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# root.left.right.left = TreeNode(6)

# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(8)

s = Solution()
print(s.rightSideView(root))

