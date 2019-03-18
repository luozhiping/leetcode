# 102. 二叉树的层次遍历
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/submissions/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        seq = []
        result = []
        if root:
            seq.append(root)
        while seq:
            tmp = []
            tmp_seq = []
            while seq:
                node = seq.pop(0)
                if node.left:
                    tmp_seq.append(node.left)
                if node.right:
                    tmp_seq.append(node.right)
                tmp.append(node.val)
            seq.extend(tmp_seq)
            result.append(tmp)

        return result




root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


s = Solution()
print(s.levelOrder(root))