# 299. 猜数字游戏
# https://leetcode-cn.com/problems/bulls-and-cows/

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = 0
        B = 0
        answer = {}
        As = []
        for i, c in enumerate(secret):
            if c == guess[i]:
                As.append(i)
                A += 1
                continue
            if c in answer:
                answer[c].append(i)
            else:
                answer[c] = [i]
        print(answer, As)
        for i, c in enumerate(guess):
            if i in As:
                continue
            if c in answer:
                answer[c].pop(0)
                B += 1
                if not answer[c]:
                    answer.pop(c)
        return "%dA%dB" % (A, B)




s = Solution()
print(s.getHint("1807", "7810"))
print(s.getHint("1123", "01111"))
print(s.getHint("011", "110"))