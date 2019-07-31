# 654. 最大二叉树
# https://leetcode-cn.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def buildLeft(root, seq):
            if seq:
                maxValue = max(seq)
                maxIndex = seq.index(maxValue)
                root.left = TreeNode(maxValue)
                buildLeft(root.left, seq[:maxIndex])
                buildRight(root.left, seq[maxIndex+1:])
        def buildRight(root, seq):
            if seq:
                maxValue = max(seq)
                maxIndex = seq.index(maxValue)
                root.right = TreeNode(maxValue)
                buildLeft(root.right, seq[:maxIndex])
                buildRight(root.right, seq[maxIndex+1:])

        maxValue = max(nums)
        maxIndex = nums.index(maxValue)
        root = TreeNode(maxValue)
        buildLeft(root, nums[:maxIndex])
        buildRight(root, nums[maxIndex+1:])
        return root

s = Solution()
print(s.constructMaximumBinaryTree([3,2,1,6,0,5]))

import random
test = []

for i in range(random.randint(500, 1000)):
    test.append(i)
random.shuffle(test)
print(test)
