# 767. 重构字符串
# https://leetcode-cn.com/problems/reorganize-string/

import heapq
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        dicts = {}
        for c in S:
            dicts[c] = dicts.get(c, 0) + 1
        array = []
        for c in dicts:
            heapq.heappush(array, [-dicts[c], c])
        cur = heapq.heappop(array)
        if abs(cur[0]) > (len(S)+1)//2:
            return ""
        heapq.heappush(array, cur)
        # print(heapq.heappop(array))
        result = ""
        while array:
            cur = heapq.heappop(array)
            result += cur[1]
            cur[0] += 1

            if array:
                cur2 = heapq.heappop(array)
                result += cur2[1]
                cur2[0] += 1
                if cur2[0] != 0:
                    heapq.heappush(array, cur2)
            if cur[0] != 0:
                heapq.heappush(array, cur)

        # print(result)
        return result




s = Solution()
print(s.reorganizeString("aab"))
assert s.reorganizeString("ogccckcwmbmxtsbmozli") == "cocgcickmlmsmtbwbxoz"
import random
