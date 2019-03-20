# 127. 单词接龙
# https://leetcode-cn.com/problems/word-ladder/

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList and endWord not in wordList:
            return 0
        queue = [beginWord]
        result = 1

        flag = [False for _ in range(len(wordList))]

        minResult = None
        while queue:
            tmp = []
            result += 1
            while queue:
                cur = queue.pop()
                for i, word in enumerate(wordList):
                    if flag[i]:
                        continue
                    dis = 0
                    for index, c in enumerate(word):
                        if c != cur[index]:
                            dis += 1
                            if dis > 1:
                                break
                    if dis == 1:
                        if word == endWord:
                            if minResult:
                                minResult = min(minResult, result)
                            else:
                                minResult = result
                            break
                        else:
                            flag[i] = True
                            tmp.append(word)
            queue.extend(tmp)
        return minResult if minResult is not None else 0


s = Solution()
print(s.ladderLength("hit",
"cog",
["hot","dot","dog","lot","log"]))