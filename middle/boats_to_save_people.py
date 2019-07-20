# 881. 救生艇
# https://leetcode-cn.com/problems/boats-to-save-people/

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people:
            return 0
        people = sorted(people)
        start = 0
        end = len(people) - 1
        result = 0

        while start < end:
            if people[start] + people[end] <= limit:
                start += 1
                end -= 1
                result += 1
            else:
                end -= 1
                result += 1
        if start == end:
            result += 1
        return result


s = Solution()
print(s.numRescueBoats([1,2], 3))

import random

test = []
limit = random.randint(1, 30000)
for i in range(random.randint(1, 50000)):
    test.append(random.randint(1, limit))

print(test, limit)
print(s.numRescueBoats(test, limit))