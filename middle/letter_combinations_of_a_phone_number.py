# 17. 电话号码的字母组合
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        alphabet = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        queue = []
        queue.extend(list(alphabet[digits[0]]))
        digits = digits[1:]
        for digit in digits:
            cur = alphabet[digit]
            tmp = []
            while queue:
                node = queue.pop(0)
                for i in range(len(cur)):
                    tmp.append(node + cur[i])
            queue.extend(tmp)
        return queue


s = Solution()
print(s.letterCombinations("23"))