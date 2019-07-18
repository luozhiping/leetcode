# 722. 删除注释
# https://leetcode-cn.com/problems/remove-comments/

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        if not source:
            return source
        result = []
        startedComment = False
        lineResult = []
        for line in source:
            while line:
                if not startedComment:
                    c1 = line.find("//")
                    c2 = line.find("/*")
                    if c1 == -1 and c2 == -1:
                        lineResult.extend(line)
                        break
                    c1 = c1 if c1 != -1 else len(line)
                    c2 = c2 if c2 != -1 else len(line)

                    if c1 < c2:
                        lineResult.extend(line[:c1])
                        break
                    startedComment = True
                    lineResult.extend(line[:c2])
                    line = line[c2+2:]
                else:
                    c = line.find("*/")
                    if c != -1:
                        startedComment = False
                        line = line[c+2:]
                    else:
                        break
            if lineResult and not startedComment:
                result.append("".join(lineResult))
                lineResult = []
        return result

s = Solution()
print(s.removeComments( ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "test/* This is a test", "   multiline  ", "   comment for ", "   testing */end", "a = b + c;", "}"]))