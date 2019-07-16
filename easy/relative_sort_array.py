# 1122. 数组的相对排序
# https://leetcode-cn.com/problems/relative-sort-array/

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        if not arr1:
            return []
        dicts = {}
        noArr2 = []
        for num in arr1:
            if num in arr2:
                dicts[num] = dicts.get(num, 0) + 1
            else:
                noArr2.append(num)
        # print(dicts, noArr2)
        result = []
        for num in arr2:
            result.extend([num]*dicts[num])
        result.extend(sorted(noArr2))
        return result


s = Solution()
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], []))