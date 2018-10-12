# 盛最多水的容器
# https://leetcode-cn.com/problems/container-with-most-water/description/


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            leftH = height[left]
            rightH = height[right]
            if leftH < rightH:
                area = (right - left) * leftH
                left += 1
            else:
                area = (right - left) * rightH
                right -= 1
            if area > maxArea:
                maxArea = area
        return maxArea

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))