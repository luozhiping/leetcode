# 423. 从英文中重建数字
# https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 1: g u w  2: f h r s   3: o   4: i t  5: n  e: 9
        if not s:
            return ""
        dicts = {}
        for c in s:
            dicts[c] = dicts.get(c, 0) + 1

        alpha = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,"six": 6, "seven": 7, "eight": 8, "nine": 9}

        one = {"g": "eight", "u": "four", "w": "two", "z": "zero", "x": "six",
               "f": "five", "h":"three", "o": "one",
               "v": "seven", "e": "nine"
               }
        result = []
        for c in one:
            count = dicts.get(c, 0)
            if count > 0:
                for iC in one[c]:
                    dicts[iC] = dicts.get(iC, 0) - count
                result.extend([str(alpha[one[c]])]*count)
        result = sorted(result)
        return "".join(result)

s = Solution()
print(s.originalDigits("owoztneoer"))
print(s.originalDigits("fviefuro"))

import random
test = []
testStr = ""
alpha = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
for i in range(random.randint(100, 10000)):
    num = random.randint(0, 9)
    test.append(str(num))
    testStr += alpha[num]
testStr = list(testStr)
random.shuffle(testStr)
print("".join(testStr))

assert s.originalDigits(testStr) == "".join(sorted(test))

