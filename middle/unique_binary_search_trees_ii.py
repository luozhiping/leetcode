# 95. 不同的二叉搜索树 II
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result = []
        def generate(start, end):
            if start > end:
                return [None]
            # if start == end:
            #     return [TreeNode(start)]
            tmp = []

            for i in range(start, end+1):
                leftTrees = generate(start, i-1)
                rightTrees = generate(i+1,end)

                for l in leftTrees:
                    for r in rightTrees:
                        current = TreeNode(i)
                        current.left = l
                        current.right = r
                        tmp.append(current)
            return tmp

        if n == 0:
            return []

        return generate(1, n)




s = Solution()
print(s.generateTrees(3))