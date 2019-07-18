# 451. 根据字符出现频率排序
# https://leetcode-cn.com/problems/sort-characters-by-frequency

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxItem = 0
        if not s:
            return s
        dict = {}
        for c in s:
            dict[c] = dict.get(c, 0) + 1
            maxItem = max(maxItem, dict[c])
        bucket = [[] for _ in range(maxItem+1)]
        # print(results)
        for key in dict:
            bucket[dict[key]].insert(0, key)
        result = ""
        for i in range(len(bucket) - 1, -1, -1):
            for key in bucket[i]:
                result += key*i
        return result

s = Solution()
print(s.frequencySort("askfjaoijowijbowiejfoiweajoibnkfvmnkdfmviIIOJAIOSOBQWYVMDMVSVKJVNIQUWHFPIJFPOQ"))