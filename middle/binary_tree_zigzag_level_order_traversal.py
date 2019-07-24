# 103. 二叉树的锯齿形层次遍历
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        toRight = True
        seq = [root]
        result = []
        while seq:
            tmp = []
            tResult = []
            while seq:
                cur = seq.pop(-1)
                tResult.append(cur.val)
                if toRight:
                    if cur.left:
                        tmp.append(cur.left)
                    if cur.right:
                        tmp.append(cur.right)
                else:
                    if cur.right:
                        tmp.append(cur.right)
                    if cur.left:
                        tmp.append(cur.left)
            seq.extend(tmp)
            toRight = not toRight
            result.append(tResult)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(8)

s = Solution()
print(s.zigzagLevelOrder(root))