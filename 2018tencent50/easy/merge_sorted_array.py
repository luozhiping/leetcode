# 合并两个有序数组
# https://leetcode-cn.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index2 = n - 1
        index1 = m - 1
        while index2 >= 0 and index1 >= 0:
            if nums2[index2] >= nums1[index1]:
                nums1.pop()
                nums1.insert(index1+1, nums2[index2])
                index2 -= 1
            else:
                index1 -= 1
        for i in range(index2, -1, -1):
            nums1.pop()
            nums1.insert(0, nums2[i])
        print(nums1)

s = Solution()
s.merge([4,5,6,0,0,0],3,[1,2,3],3)