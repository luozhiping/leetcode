# 116. 填充每个节点的下一个右侧节点指针
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node

# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        seq = [root]

        while seq:
            tmp = []
            for i in range(len(seq)):
                if i < len(seq) - 1:
                    seq[i].next = seq[i + 1]
                if seq[i].left:
                    tmp.append(seq[i].left)
                if seq[i].right:
                    tmp.append(seq[i].right)
            seq = tmp
        return root




root = Node(1,
        Node(2, Node(4, None, None, None), Node(5, None, None, None), None),
        Node(3, Node(6, None, None, None), Node(7, None, None, None), None),
        None
        )

s = Solution()
print(s.connect(root))