# 973. 最接近原点的 K 个点
# https://leetcode-cn.com/problems/k-closest-points-to-origin/

class Solution2(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if len(points) == K:
            return points
        distance = {}
        for point in points:
            dis = point[0]**2+point[1]**2
            if dis in distance:
                distance[dis].append(point)
            else:
                distance[dis] = [point]
        keys = sorted(distance.keys())
        result = []
        for key in keys:
            seq = distance[key]
            result.extend(seq[:K])
            K -= len(seq)
            if K <= 0:
                return result
        return result


s = Solution()
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))


import random

test = []
for i in range(random.randint(1, 10000)):
    test.append([random.randint(-10000, 10000), random.randint(-10000, 10000)])
K = random.randint(1, len(test))
print(test, K)
print(s.kClosest(test, K))