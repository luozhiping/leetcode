# 1008. 先序遍历构造二叉树
# https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def buildTree(root, neworder, isLeft):
            if isLeft:
                root.left = TreeNode(neworder[0])
                root = root.left
            else:
                root.right = TreeNode(neworder[0])
                root = root.right
            right = len(neworder)
            for i in range(1, len(neworder)):
                if neworder[i] > neworder[0]:
                    right = i
                    break
            left = neworder[1:right]
            right = neworder[right:]
            if len(left) > 0:
                buildTree(root, left, True)
            if len(right) > 0:
                buildTree(root, right, False)


        tree = TreeNode(preorder[0])
        right = len(preorder)
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                right = i
                break

        print(preorder[1:right], preorder[right:])
        left = preorder[1:right]
        right = preorder[right:]
        if len(left) > 0:
            buildTree(tree, left, True)
        if len(right) > 0:
            buildTree(tree, right, False)




        return tree


s = Solution()
result = s.bstFromPreorder([8,5,1,7,10,12])
print(result.val)