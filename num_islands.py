# coding:utf-8
import collections

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def numIslands(grid):
    if not grid or not grid[0]: # [] or [ [] ]
        return 0
    islands = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] and (i, j) not in visited:
                bfs(grid, i, j, visited)
                islands += 1
    return islands

def bfs(grid, x, y, visited):
    # 从一块土地出发，通过BFS，遍历整个岛屿
    queue = collections.deque([(x, y)])
    visited.add((x, y))
    while queue:
        x, y = queue.popleft()
        for delta_x, delta_y in DIRECTIONS:
            next_x = x + delta_x
            next_y = y + delta_y
            if not is_valid(grid, next_x, next_y, visited):
                continue
            queue.append((next_x, next_y))
            visited.add((next_x, next_y))

def is_valid(grid, x, y, visited):
    n, m = len(grid), len(grid[0])
    if not (0 <= x < n and 0 <= y < m):
        return False
    if (x, y) in visited:
        return False

    return grid[x][y] # 0-False 1-True

if __name__ == '__main__':
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]

    print(numIslands(grid))

