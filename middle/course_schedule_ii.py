# 210. 课程表 II
# https://leetcode-cn.com/problems/course-schedule-ii/

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        tuopu = {}
        du = [0 for _ in range(numCourses)]
        stack = []
        for pre in prerequisites:
            if pre[1] in tuopu:
                tuopu[pre[1]].append(pre[0])
            else:
                tuopu[pre[1]] = [pre[0]]
            du[pre[0]] += 1
        result = []
        for i in range(len(du)):
            if du[i] == 0:
                stack.append(i)
                du[i] = -1
            while stack:
                index = stack.pop(0)
                result.append(index)
                if index in tuopu:
                    for n in tuopu[index]:
                        du[n] -= 1
                        if du[n] == 0:
                            stack.append(n)
                            du[n] = -1
        return result if len(result) == numCourses else []

s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))