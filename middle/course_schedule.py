# 207. 课程表
# https://leetcode-cn.com/problems/course-schedule

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        board = [set() for _ in range(numCourses)]
        du = [0 for _ in range(numCourses)]
        for pre in prerequisites:
            board[pre[1]].add(pre[0])
            du[pre[0]] += 1
        # print(board, du)

        seq = []
        for i in range(len(du)):
            if du[i] == 0:
                seq.append(i)

        counter = 0
        while seq:
            index = seq.pop(0)
            counter += 1
            for t in board[index]:
                du[t] -= 1
                if du[t] == 0:
                    seq.append(t)

        return counter == numCourses

s = Solution()
print(s.canFinish(3, [[1,0],[2,1]]))