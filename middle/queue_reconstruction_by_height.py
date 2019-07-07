# 406. 根据身高重建队列
# https://leetcode-cn.com/problems/queue-reconstruction-by-height/
import  functools

class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        def sortFunc(x, y):
            if x[0] != y[0]:
                return x[0] - y[0]
            return y[1] - x[1]

        if not people:
            return []
        people = sorted(people, key = functools.cmp_to_key(sortFunc))
        print(people)
        value = people.pop(-1)
        result = []
        while value:
            result.insert(value[1], value)
            if not people:
                break
            value = people.pop(-1)
        return result


s = Solution()
print(s.reconstructQueue([[7,0]]))