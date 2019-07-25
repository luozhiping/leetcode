# 117. 填充每个节点的下一个右侧节点指针 II
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/


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
        last = root
        current = None
        currentHead = None
        while last:
            if last.left:
                if current:
                    current.next = last.left
                    current = last.left
                else:
                    currentHead = last.left
                    current = last.left
            if last.right:
                if current:
                    current.next = last.right
                    current = last.right
                else:
                    currentHead = last.right
                    current = last.right
            if last.next:
                last = last.next
            elif currentHead:
                last = currentHead
                current = None
                currentHead = None
            else:
                break
        return root


root = Node(1, Node(2, Node(4, None,None,None),Node(5,None,None,None),None),Node(3,None,Node(7,None,None,None),None),None)
s = Solution()
print(s.connect(root))