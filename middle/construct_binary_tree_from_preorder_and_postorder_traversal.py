# 889. 根据前序和后序遍历构造二叉树
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None
        def construct(node, pre, post):
            if not pre:
                return
            val = pre[0]
            index = post.index(val)

            if index != len(post) - 1:
                node.left = TreeNode(val)
                construct(node.left, pre[1:index+1], post[:index])
                rightVal = pre[index+1]
                node.right = TreeNode(rightVal)
                construct(node.right, pre[index+2:],post[index+1:-1])
            else:
                node.right = TreeNode(val)
                construct(node.right, pre[1:], post[:-1])




        root = TreeNode(pre[0])
        construct(root, pre[1:], post[:-1])
        return root

s = Solution()
node = s.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])
print(node.val)