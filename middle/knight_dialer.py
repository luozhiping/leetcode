# 935. 骑士拨号器
# https://leetcode-cn.com/problems/knight-dialer/

class Solution2(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 10
        bp = [[0 for _ in range(10)] for _ in range(N+1)]
        bp[1] = [1 for _ in range(10)]
        bp[0] = [1 for _ in range(10)]
        # print(bp)
        nextStep = {0:[4, 6], 1:[8, 6], 2:[7, 9],
                    3:[4, 8], 4:[3, 9, 0], 5:[],
                    6:[1, 7, 0], 7:[2, 6], 8:[1, 3], 9:[2, 4]}
        def bps(cur, step):
            if step == 0:
                return 0
            if step == 1:
                return 1
            result = 0
            for n in nextStep[cur]:
                if bp[step-1][n] != -1:
                    result += bp[step-1][n]
                else:
                    tmp = bps(n, step - 1)
                    result += tmp
            bp[step][cur] = result
            return result

        r = 0
        for i in range(10):
            r += bps(i, N)
        # print(r)
        return r % (10**9 + 7)

class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return 10
        # bp = [[-1 for _ in range(10)] for _ in range(N+1)]
        # bp[1] = [1 for _ in range(10)]
        last = [1 for _ in range(10)]
        cur = [1 for _ in range(10)]
        # bp[0] = [1 for _ in range(10)]
        # print(bp)
        nextStep = {0:[4, 6], 1:[8, 6], 2:[7, 9],
                    3:[4, 8], 4:[3, 9, 0], 5:[],
                    6:[1, 7, 0], 7:[2, 6], 8:[1, 3], 9:[2, 4]}

        for i in range(2, N + 1):
            for j in range(10):
                tmp = 0
                for n in nextStep[j]:
                    tmp += last[n]
                cur[j] = tmp
            t = last
            last = cur
            cur = t

        # print(sum(last))
        return sum(last) % (10**9 + 7)

s = Solution()
# assert s.knightDialer(1) == 10
# assert s.knightDialer(2) == 20
assert s.knightDialer(3) == 46
print(s.knightDialer(4960))
