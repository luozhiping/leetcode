# 222. 完全二叉树的节点个数
# https://leetcode-cn.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        seq = [root]
        result = 0
        while seq:
            tmp = []
            while seq:
                cur = seq.pop(0)
                result += 1
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            seq.extend(tmp)
        return result



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

s = Solution()
assert s.countNodes(root) == 6