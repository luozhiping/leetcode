# 274. H指数
# https://leetcode-cn.com/problems/h-index/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        return len(citations)


s = Solution()
print(s.hIndex([3,0,6,1,5]))