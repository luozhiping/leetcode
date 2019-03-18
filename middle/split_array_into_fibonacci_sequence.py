# 842. 将数组拆分成斐波那契序列
# https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/

class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        maxNum = 2**31 - 1
        if not S or len(S) < 3:
            return []
        length = (len(S) - 1) // 2
        def findFib(first, second, restStr, result):
            last = int(first) + int(second)
            if last > maxNum:
                return []
            lastStr = str(last)
            if lastStr == restStr:
                result.append(int(lastStr))
                return result
            if restStr[:len(lastStr)] == lastStr:
                result.append(int(lastStr))
                return findFib(second, last, restStr[len(lastStr):], result)
            return []
        for i in range(1, length+1):
            firstNum = S[:i]
            if firstNum[0] == "0" and i > 1:
                break
            # print(firstNum)
            if int(firstNum) > maxNum:
                break
            for j in range(1, length+1):
                secondNum = S[i:i+j]
                if secondNum[0] == "0" and j > 1:
                    continue
                if int(secondNum) > maxNum:
                    break
                result = []
                result.append(int(firstNum))
                result.append(int(secondNum))
                if findFib(firstNum, secondNum, S[i+j:], result):
                    return result
        return []



        # while True:


s = Solution()
print(s.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))
