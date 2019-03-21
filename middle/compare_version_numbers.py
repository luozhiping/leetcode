# 165. 比较版本号
# https://leetcode-cn.com/problems/compare-version-numbers/

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        while len(v1) < len(v2):
            v1.append(0)
        while len(v2) < len(v1):
            v2.append(0)
        index = 0
        # print(v1, v2)
        while index < len(v1):
            if int(v1[index]) > int(v2[index]):
                return 1
            elif int(v1[index]) < int(v2[index]):
                return -1
            else:
                index += 1
        return 0

s = Solution()
print(s.compareVersion("1", "1"))