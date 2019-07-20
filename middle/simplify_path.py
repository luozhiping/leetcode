# 71. 简化路径
# https://leetcode-cn.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        result = []
        needGang = True
        paths = path.split("/")
        for p in paths:
            if p == "" or p == ".":
                continue
            if p == "..":
                if result:
                    result.pop(-1)
            else:
                result.append(p)

        return "/" + "/".join(result)

s = Solution()
assert s.simplifyPath("/home//foo/") == "/home/foo"
assert s.simplifyPath("/home/") == "/home"
assert s.simplifyPath("/../") == "/"
assert s.simplifyPath("/a/../../b/../c//.//") == "/c"
assert s.simplifyPath("/a/./b/../../c/") == "/c"
assert s.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"