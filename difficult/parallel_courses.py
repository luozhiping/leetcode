# 1136. 平行课程
# https://leetcode-cn.com/problems/parallel-courses/
class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        rudu = {}
        ru = [0 for _ in range(N)]
        chudu = {}
        chu = [0 for _ in range(N)]
        for re in relations:
            if re[1] in rudu:
                rudu[re[1]].append(re[0])
            else:
                rudu[re[1]] = [re[0]]
            if re[0] in chudu:
                chudu[re[0]].append(re[1])
            else:
                chudu[re[0]] = [re[1]]
            ru[re[1] - 1] += 1
            chu[re[0] - 1] += 1
        print(rudu, ru, chudu, chu)
        result = 0
        learned = [False for _ in range(N)]
        while True:
            result += 1
            hasNoLearned = False
            hasNoChu = True
            for i in range(N):
                if chu[i] == 0:
                    if i+1 in rudu:
                        for ru in rudu[i+1]:
                            chu[ru-1] -= 1
                            chudu[ru].remove(i+1)
                        rudu.pop(i + 1)
                    if not learned[i]:
                        hasNoChu = False
                    learned[i] = True
                else:
                    hasNoLearned = True
            if not hasNoLearned:
                break
            if hasNoChu:
                return -1

        return result
s = Solution()
print(s.minimumSemesters(3, [[1,3],[2,3]]))
print(s.minimumSemesters(3, [[1,2],[2,3],[3,1]]))