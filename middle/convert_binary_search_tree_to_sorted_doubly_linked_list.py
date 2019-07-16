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
        def inorder(pre, post, node):
            first = None
            last = None
            if node.left:
                f, l = inorder(None, node, node.left)
                if l:
                    last = l
            print(node.val)
            if node.right:
                f, l = inorder(node, None, node.right)
                if f:
                    first = f
            if last:
                print(node.val, "pre:", last.val)
                # pre.right = node
                # node.left = pre
            else:
                print(node.val, "pre:", pre.val)
            if first:
                print(node.val, "post:", first.val)
                # post.left = node
                # node.right = post
            else:
                print(node.val, "post:", post.val)
            # print(node.val, "no pre no post:")
            if not last:
                last = node
            if not first:
                first = node
            return first, last

        inorder(None, None, root)

        return root

root = Node(4, Node(2, Node(1, None, None), Node(3, None, None)), Node(5, None, None))
# root.left = Node(2)
# root.right = Node(5)
# root.left.left = Node(1)
# root.left.right = Node(3)

s = Solution()
result = s.treeToDoublyList(root)