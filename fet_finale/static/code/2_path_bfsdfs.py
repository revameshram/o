from collections import deque

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)
goal = (3, 3)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None


def dfs():
    stack = []
    stack.append((start, [start]))
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == goal:
            return path

        if (x, y) not in visited:
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 0 and (nx, ny) not in visited:
                        stack.append(((nx, ny), path + [(nx, ny)]))

    return None


print("Grid:")
for row in grid:
    print(row)

print("BFS Path:")
bfs_path = bfs()
print(bfs_path)

print("\nDFS Path:")
dfs_path = dfs()
print(dfs_path)
