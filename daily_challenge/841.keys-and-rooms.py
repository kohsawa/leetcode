#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#
import collections

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        q = collections.deque([0])
        visited = {0}
        
        while q:
            r = q.popleft()

            for n in rooms[r]:
                if n in visited:
                    continue
                visited.add(n)
                q.append(n)
        return len(visited) >= len(rooms)

# @lc code=end

