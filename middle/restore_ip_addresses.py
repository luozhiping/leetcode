# 93. 复原IP地址
# https://leetcode-cn.com/problems/restore-ip-addresses/

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        result = []
        def dfs(string, tmp="", depth=1):
            if not string:
                return
            if depth == 3:

                if int(string) <= 255:
                    if len(string) > 1:
                        if string[0] != '0':
                            result.append(tmp+"."+string)
                    else:
                        result.append(tmp+"."+string)
                return
            if string[0] == '0':
                dfs(string[1:], tmp + '.0', depth+1)
            else:
                for i in range(1, 4):
                    if int(string[:i]) <= 255:
                        dfs(string[i:], tmp + "." + string[:i], depth+1)


        if s[0] == '0':
            dfs(s[1:], '0', 1)
        else:
            for i in range(1, 4):
                if int(s[:i]) <= 255:
                    dfs(s[i:], s[:i], 1)
                else:
                    continue
        # print(result)
        return result

s = Solution()
assert s.restoreIpAddresses("1111") == ["255.255.11.135", "255.255.111.35"]