# 139. 单词拆分
# https://leetcode-cn.com/problems/word-break/

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        canFinded = [True for _ in range(len(s)+1)]
        def dfs(index):
            if not canFinded[index]:
                return False
            for i in range(index+1, len(s)+1):
                string = s[index:i]
                if string in wordDict:
                    if i == len(s):
                        return True
                    if dfs(i):
                        return True
            canFinded[index] = False
            return False



        for i in range(1, len(s)+1):
            string = s[:i]
            if string in wordDict:
                # print(string)
                if i == len(s):
                    return True
                if dfs(i):
                    return True
        return False


s = Solution()
assert s.wordBreak("leetcode", ["leet", "code"]) == True
assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
assert s.wordBreak("applepenapple", ["apple", "pen"]) == True
assert s.wordBreak("", ["leet", "code"]) == False