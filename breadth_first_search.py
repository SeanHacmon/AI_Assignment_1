import pandas as pd
from collections import deque

# The function initializes and returns open
def init_open():
    return deque()

# The function inserts s into open
def insert_to_open(open_list, s):  # Should be implemented according to the open list data structure
    open_list.append(s)

# The function returns the best node in open (according to the search algorithm)
def get_best(open_list):
    return open_list[0]

# The function returns neighboring locations of s_location
def get_neighbors(grid, s_location):
    # initialize
    neighbors = []
    x = s_location[0]
    y = s_location[1]

    # right
    if grid[x+1][y] != '@' and valid_move(grid, x+1, y):
        neighbors.append(grid[x+1][y])
    # down
    if grid[x][y+1] != '@' and valid_move(grid, x, y+1):
        neighbors.append(grid[x+1][y])
    # left
    if grid[x-1][y] != '@' and valid_move(grid, x-1, y):
        neighbors.append(grid[x+1][y])
    # up
    if grid[x][y-1] != '@' and valid_move(grid, x, y-1):
        neighbors.append(grid[x+1][y])
    return neighbors

# The function returns whether n_location should be generated (checks in open_list)
# removes a node from open_list if needed 
def check_for_duplicates_open(n_location, s, open_list):
    return False
  
# The function returns whether n_location should be generated (checks in closed_list)
# removes a node from closed_list if needed  
def check_for_duplicates_close(n_location, s, closed_list):
    return n_location in closed_list

# The function returns whether or not s_location is the goal location
def is_goal(s_location, goal_location):
    return (s_location[0] == goal_location[0]) and (s_location[1] == goal_location[1])

# Locations are tuples of (x, y)
def bfs(grid, start_location, goal_location):
    # State = (x, y, s_prev)
    # Start_state = (x_0, y_0, False)
    open_list = init_open()
    closed_list = {}

    # Mark the source node as
    # visited and enqueue it
    start = (start_location[0], start_location[1], False)
    insert_to_open(open_list, start)

    while not open_list.empty():
        # Dequeue a vertex from
        # queue and print it
        s = get_best(open_list)
        # print(s, end=" ")
        s_location = (s[0], s[1])
        if s_location in closed_list:
            continue
        if is_goal(s_location, goal_location):
            print("The number of states visited by BFS:", len(closed_list))
            return s
        neighbors = get_neighbors(grid, s_location)
        for n_location in neighbors:
            if check_for_duplicates_open(n_location, s, open_list) or check_for_duplicates_close(n_location, s, closed_list):
                continue
            n = (n_location[0], n_location[1], s)
            insert_to_open(open_list, n)
        closed_list[s_location] = s

def print_route(s):
    while s:
        print(s[0], s[1])
        s = s[3]

def get_route(s):
    route = []
    while s:
        s_location = (s[0], s[1])
        route.append(s_location)
        s = s[2]
    route.reverse()
    return route

def print_grid_route(route, grid):
    for location in route:
        grid[location] = 'x'
    print(pd.DataFrame(grid))

# Sean Functions
def valid_move(grid, x, y):
    row = len(grid)
    col = len(grid[0])
    return (0 <= x < row) and (0 <= y < col)
