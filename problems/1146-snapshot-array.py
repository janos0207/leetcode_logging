# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:
    def __init__(self, length: int):
        self.current = {}
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.current[index] = val

    def snap(self) -> int:
        self.snaps.append(self.current.copy())
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        dic = self.snaps[snap_id]
        return dic.get(index, 0)
