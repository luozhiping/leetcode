# 841. 钥匙和房间
# https://leetcode-cn.com/problems/keys-and-rooms/

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms:
            return False

        self.result = 0
        def dfs(rooms, keys, room, i):
            room[i] = True
            self.result += 1
            for key in keys:
                if room[key]:
                    continue
                else:
                    dfs(rooms, rooms[key], room, key)

        result = 0
        room = [False for _ in range(len(rooms))]
        # print(sum(room))
        dfs(rooms, rooms[0], room, 0)
        if self.result == len(rooms):
            return True
        return False

s = Solution()
print(s.canVisitAllRooms([[]]))