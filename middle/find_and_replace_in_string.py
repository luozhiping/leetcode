# 833. 字符串中的查找与替换
# https://leetcode-cn.com/problems/find-and-replace-in-string/

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        if not indexes:
            return S
        if not S:
            return S
        dicts = {}
        for i in range(len(indexes)):
            dicts[indexes[i]] = (sources[i], targets[i])
        # print(dicts)
        keys = sorted(dicts.keys(), reverse=True)
        # print(keys)
        # lastKey = len(S)
        for key in keys:
            source, target = dicts[key]
            if S[key:key+len(source)] == source:
                S = S[:key] + S[key:].replace(source, target, 1)
            # lastKey = key
        return S




s = Solution()
print(s.findReplaceString("abcd", [0,2], ["a","cd"], ["eee","ffff"]))
print(s.findReplaceString("abcd", [0,2], ["ab","ec"], ["eee","ffff"]))
print(s.findReplaceString("jjievdtjfb",
[4,6,1],
["md","tjgb","jf"],
["foe","oov","e"]))