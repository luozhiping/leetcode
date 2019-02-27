# 969. 煎饼排序
# https://leetcode-cn.com/problems/pancake-sorting/

class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if A is None:
            return None
        if len(A) == 1:
            return A
        reverseCount = 0
        result = []
        while reverseCount < len(A):
            max_index = 0
            max = A[0]
            for index in range(len(A) - reverseCount):
                a = A[index]
                if a > max:
                    max = a
                    max_index = index
            r = self.fadePan(A, max_index, reverseCount)
            if r:
                result.extend(r)
            reverseCount += 1
        return result

    def fadePan(self, A, fadeIndex, reverseCount):
        if fadeIndex == len(A) - reverseCount:
            return None
        result = []
        #print(A)
        if fadeIndex != 0:
            for i in range((fadeIndex+1)//2):
                A[i], A[fadeIndex-i] = A[fadeIndex-i], A[i]

            print('2',A, fadeIndex)
            result.append(fadeIndex+1)
        for i in range((len(A)-reverseCount)//2):
            A[i], A[(len(A)-reverseCount) - 1 - i] = A[(len(A)-reverseCount) - 1 - i], A[i]
        result.append(len(A) - reverseCount)
        print('3:', A, len(A) - reverseCount)
        return result



s = Solution()
print(s.pancakeSort([3,2,4,1]))