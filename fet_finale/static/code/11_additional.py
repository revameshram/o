import heapq
import math

# Directions: up, down, left, right
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# Goal state
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Find position of a value in goal
def find_pos(value):
    for i in range(3):
        for j in range(3):
            if goal[i][j] == value:
                return i, j

# Manhattan heuristic
def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x, y = find_pos(val)
                dist += abs(i - x) + abs(j - y)
    return dist

# Euclidean heuristic
def euclidean(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x, y = find_pos(val)
                dist += math.sqrt((i - x)**2 + (j - y)**2)
    return dist

# Convert state to tuple (for hashing)
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Find empty tile
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# A* Algorithm
def astar(start, heuristic):
    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()

    while pq:
        cost, state = heapq.heappop(pq)

        if state == goal:
            return cost

        visited.add(to_tuple(state))
        x, y = find_zero(state)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                if to_tuple(new_state) not in visited:
                    g = cost + 1
                    h = heuristic(new_state)
                    heapq.heappush(pq, (g + h, new_state))

    return -1

# Example start state
start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

print("Manhattan Cost:", astar(start, manhattan))
print("Euclidean Cost:", astar(start, euclidean))




#something about block is these:
# Example: blocks stacked as lists
# Each stack is a list, last element is top

# goal = [['A', 'B', 'C'], []]

# # Custom heuristic
# def custom_heuristic(state):
#     score = 0
    
#     # Penalize misplaced blocks
#     for i in range(len(state)):
#         for j in range(len(state[i])):
#             if i >= len(goal) or j >= len(goal[i]) or state[i][j] != goal[i][j]:
#                 score += 1
    
#     return score

# # Example states
# state1 = [['A','C','B'], []]
# state2 = [['A','B'], ['C']]

# print("Heuristic state1:", custom_heuristic(state1))
# print("Heuristic state2:", custom_heuristic(state2))