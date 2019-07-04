# 146. LRU缓存机制
# https://leetcode-cn.com/problems/lru-cache/
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return - 1

        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.dict.move_to_end(key)
        self.dict[key] = value
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2);
print(cache.get(1))
cache.put(3, 3);
print(cache.get(2))
cache.put(4, 4);
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)