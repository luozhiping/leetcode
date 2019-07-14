# 797. 所有可能的路径
# https://leetcode-cn.com/problems/all-paths-from-source-to-target/

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if not graph:
            return None
        result = []
        def dfs(graph, cur, cur_list):
            if cur == len(graph) - 1:
                result.append(cur_list)
                return

            next = graph[cur]
            for n in next:
                l = list(cur_list)
                l.append(n)
                dfs(graph, n, l)


        dfs(graph, 0, [0])

        return result



s = Solution()
print(s.allPathsSourceTarget([[1,2], [3], [3], []]))