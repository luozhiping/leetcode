# 105. 从前序与中序遍历序列构造二叉树
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        def buildTree(preseq, inseq):
            # print(preseq, inseq)
            if not preseq:
                return
            node = TreeNode(preseq[0])
            node.left = buildTree(preseq[1:1 + inseq.index(node.val)], inseq[:inseq.index(node.val)])
            node.right = buildTree(preseq[1 + inseq.index(node.val):], inseq[inseq.index(node.val) + 1:])
            return node

        root = TreeNode(preorder[0])
        root.left = buildTree(preorder[1:1+inorder.index(root.val)], inorder[:inorder.index(root.val)])
        root.right = buildTree(preorder[1+inorder.index(root.val):], inorder[inorder.index(root.val)+1:])
        return root

s = Solution()
node = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
print(node.val)