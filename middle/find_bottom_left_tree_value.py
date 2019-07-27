# 513. 找树左下角的值
# https://leetcode-cn.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        seq = [root]
        while seq:
            result = seq[0].val
            tmp = []
            while seq:
                cur = seq.pop(0)
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
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)


s = Solution()
assert  s.findBottomLeftValue(root) == 7

