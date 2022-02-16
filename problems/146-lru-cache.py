# https://leetcode.com/problems/lru-cache/

class DLList:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.value = value
        self.key = key

    def __repr__(self):
        return f"{self.key}: {self.value}"


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DLList(0, 0)
        self.tail = DLList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if node is None:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node:
            node.value = value
            self._move_to_head(node)
            return
        if len(self.cache) == self.capacity:
            removed_key = self._remove_tail()
            del self.cache[removed_key]
        node = DLList(key, value)
        self.cache[key] = node
        self._insert_to_head(node)

    def _move_to_head(self, node: DLList):
        self._remove_node(node)
        self._insert_to_head(node)

    def _remove_tail(self) -> int:
        node = self.tail.prev
        prev = node.prev
        prev.next = self.tail
        self.tail.prev = prev
        return node.key

    def _remove_node(self, node: DLList):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _insert_to_head(self, node: DLList):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
