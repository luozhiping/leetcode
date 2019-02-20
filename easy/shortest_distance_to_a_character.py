# 821. 字符的最短距离
# https://leetcode-cn.com/problems/shortest-distance-to-a-character/

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pos = []
        l = len(S)
        for i in range(l):
            if S[i] == C:
                pos.append(i)

        result = []
        for i in range(l):
            for j in range(len(pos)):
                if i <= pos[j]:
                    if j == 0:
                        result.append(pos[j] - i)
                        break
                    else:
                        result.append(min(pos[j] - i , i - pos[j - 1]))
                        break
                else:
                    if j == len(pos) - 1:
                        result.append(i - pos[j])
                        break
        return result

s = Solution()
print(s.shortestToChar("abba", "b"))