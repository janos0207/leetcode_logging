# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    # improved
    def isRobotBounded(self, instructions: str) -> bool:
        def move(pos, d):
            for inst in instructions:
                if inst == "G":
                    pos = [pos[0]+d[0], pos[1]+d[1]]
                elif inst == "L":
                    d = [-d[1], d[0]]
                else:  # inst == "R"
                    d = [d[1], -d[0]]
            return pos, d

        pos = [0, 0]
        d = [0, 1]
        pos, d = move(pos, d)
        return pos == [0, 0] or d != [0, 1]

    # original
    def isRobotBounded2(self, instructions: str) -> bool:
        def move(pos, d):
            for inst in instructions:
                if inst == "G":
                    pos = [pos[0]+d[0], pos[1]+d[1]]
                elif inst == "L":
                    d = [-d[1], d[0]]
                else:  # inst == "R"
                    d = [d[1], -d[0]]
            return pos, d

        pos = [0, 0]
        d = [0, 1]
        for _ in range(4):
            pos, d = move(pos, d)
        return pos == [0, 0]
