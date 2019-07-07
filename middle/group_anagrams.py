# 49. 字母异位词分组
# https://leetcode-cn.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        result = {}
        for string in strs:
            # tmp = [0 for _ in range(26)]
            key = "".join(sorted(string))
            if key in result:
                result[key].append(string)
            else:
                result[key] = [string]
            # print("".join(sorted(string)))
            # for c in string:
                # tmp[ord(c) - 97]
        # print(result)
        r = []
        for key in result:
            r.append(result[key])
        return r



s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))