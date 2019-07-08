# 394. 字符串解码
# https://leetcode-cn.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        repeat = []
        kuo = []

        tmpNum = []
        for c in s:
            if c.isnumeric():
                tmpNum.append(c)
                # repeat.append(int(c))
            elif c == '[':
                repeat.append(int("".join(tmpNum)))
                tmpNum = []
                kuo.append(c)
            elif c.isalpha():
                kuo.append(c)
            elif c == ']':
                tmp = []
                a = kuo.pop(-1)
                while a != "[":
                    tmp.insert(0, a)
                    a = kuo.pop(-1)
                re = repeat.pop(-1)
                for i in range(re):
                    kuo.append("".join(tmp))
        return "".join(kuo)





s = Solution()

print(s.decodeString("100[leetcode]"))
print(s.decodeString("3[a2[c]]"))
print(s.decodeString("2[abc]3[cd]ef"))