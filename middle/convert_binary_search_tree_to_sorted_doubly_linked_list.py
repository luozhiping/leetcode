# 426. 将二叉搜索树转化为排序的双向链表
# https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        def inorder(pre, post, node):
            first = None
            last = None
            if node.left:
                f, l = inorder(pre, node, node.left)
                if l:
                    pre = l
                first = f
            # print(node.val)
            if node.right:
                f, l = inorder(node, post, node.right)
                if f:
                    post = f
                last = l

            # print(node.val, "no pre no post:")
            if not last:
                last = node
            if not first:
                first = node
            if pre:
                # print(node.val, "pre:", pre.val)
                pre.right = node
                node.left = pre
            if post:
                # print(node.val, "post:", post.val)
                post.left = node
                node.right = post
            return first, last

        f, l = inorder(None, None, root)
        if not f:
            f = root
        if not l:
            l = root
        f.left = l
        l.right = f

        return f

# root = Node(4, None, None)
# root = Node(4, Node(2, Node(1, None, None), Node(3, None, None)), Node(5, None, None))
root = Node(6, Node(4, Node(1, None, Node(3, None, None)), Node(5, None, None)), Node(9, Node(7, None, None), None))

# root.left = Node(2)
# root.right = Node(5)
# root.left.left = Node(1)
# root.left.right = Node(3)

s = Solution()
result = s.treeToDoublyList(root)
for i in range(10):
    print(result.val)
    result = result.right