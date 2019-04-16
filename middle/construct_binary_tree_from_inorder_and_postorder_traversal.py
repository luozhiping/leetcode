# 106. 从中序与后序遍历序列构造二叉树
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        def build(ino, posto):
            node = posto[-1]
            left = ino.index(node)

            node = TreeNode(node)

            leftInorder = ino[:left]
            if len(leftInorder):
                leftPostorder = posto[:len(leftInorder)]
                node.left = build(leftInorder, leftPostorder)

            rightInorder = ino[left + 1:]
            if len(rightInorder):
                rightPostorder = posto[len(leftInorder):-1]
                node.right = build(rightInorder, rightPostorder)
            return node

        # a = []
        root = postorder[-1]
        left = inorder.index(root)

        root = TreeNode(root)

        leftInorder = inorder[:left]
        if len(leftInorder):
            leftPostorder = postorder[:len(leftInorder)]
            root.left = build(leftInorder, leftPostorder)

        rightInorder = inorder[left+1:]
        if len(rightInorder):
            rightPostorder = postorder[len(leftInorder):-1]
            root.right = build(rightInorder, rightPostorder)

        return root




s = Solution()
node = s.buildTree([9,3,15,20,7], [9,15,7,20,3])
print(node.val)