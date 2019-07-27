# 725. 分隔链表
# https://leetcode-cn.com/problems/split-linked-list-in-parts/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:

            return [None]*k
        cur = root
        count = 0
        result = []
        while cur:
            count += 1
            cur = cur.next
        if count < k:
            while root:
                tmp = root.next
                result.append(root)
                root.next = None
                root = tmp
            for i in range(k-count):
                result.append(None)
        else:
            every = count//k
            rest = count%k
            print(every, rest)
            nextHead = root
            for i in range(k):
                curHead = nextHead
                for j in range(every-1):
                    nextHead = nextHead.next
                if i < rest:
                    nextHead = nextHead.next
                result.append(curHead)
                tmp = nextHead.next
                nextHead.next = None
                nextHead = tmp

        # for re in result:
        #     r = []
        #     while re:
        #         r.append(re.val)
        #         re = re.next
        #     print(r)

        return result


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
root.next.next.next.next.next = ListNode(6)
root.next.next.next.next.next.next = ListNode(7)
root.next.next.next.next.next.next.next = ListNode(8)
root.next.next.next.next.next.next.next.next = ListNode(9)
root.next.next.next.next.next.next.next.next.next = ListNode(10)



s = Solution()
print(s.splitListToParts(root, 5))