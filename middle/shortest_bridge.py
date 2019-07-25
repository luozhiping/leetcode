# 934. 最短的桥
# https://leetcode-cn.com/problems/shortest-bridge/

class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        island = []
        finded = False
        for i in range(len(A)):
            if finded:
                break
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    island.append([i, j])
                    seq = [[i, j]]
                    A[i][j] = -1
                    while seq:
                        tmp = []
                        while seq:
                            cur = seq.pop(0)
                            for dir in dirs:
                                next = [cur[0] + dir[0], cur[1] + dir[1]]
                                if next[0] < 0 or next[0] == len(A) \
                                        or next[1] < 0 or next[1] == len(A[0])\
                                        or A[next[0]][next[1]] != 1:
                                    continue
                                tmp.append(next)
                                island.append(next)
                                A[next[0]][next[1]] = -1
                        seq.extend(tmp)
                    finded = True
                    break
        # print(sorted(island))
        result = 0
        while island:
            tmp = []
            while island:
                cur = island.pop(0)
                for dir in dirs:
                    next = [cur[0] + dir[0], cur[1] + dir[1]]
                    if next[0] < 0 or next[0] == len(A) \
                            or next[1] < 0 or next[1] == len(A[0]) \
                            or A[next[0]][next[1]] == -1:
                        continue
                    if A[next[0]][next[1]] == 0:
                        tmp.append(next)
                        A[next[0]][next[1]] = -1
                    else:
                        return result
            island.extend(tmp)
            result += 1
        return result



s = Solution()
assert s.shortestBridge([[1,1,1,1,1],
                         [1,0,0,0,1],
                         [1,0,1,0,1],
                         [1,0,0,0,1],
                         [1,1,1,1,1]]) == 1
assert s.shortestBridge([[0,1],[1,0]]) == 1
assert s.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]) == 2