import pandas as pd
import heapq
# The function initializes and returns open
def init_open():
    heap = []
    # Created a heap.
    heapq.heapify(heap)
    return heap

# The function inserts s into open
def insert_to_open(open_list, s):  # Should be implemented according to the open list data structure
    heapq.heappush(open_list, s)
    heapq.heapify(open_list)

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
    if valid_move(grid, x + 1, y):
        if grid[x+1, y] != '@':
            neighbors.append((x+1, y))
    # down
    if valid_move(grid, x, y + 1):
        if grid[x, y+1] != '@':
            neighbors.append((x, y+1))
    # left
    if valid_move(grid, x-1, y):
        if grid[x - 1, y] != '@':
            neighbors.append((x-1, y))
    # up
    if valid_move(grid, x, y-1):
        if grid[x, y - 1] != '@':
            neighbors.append((x, y-1))
    return neighbors

# The function returns whether or not s_location is the goal location
def is_goal(s_location, goal_location):
    return (s_location[0] == goal_location[0]) and (s_location[1] == goal_location[1])

# The function estimates the cost to get from s_location to goal_location
def calculate_heuristic(s_location, goal_location):
    # Pitagoras
    return ((goal_location[0] - s_location[0])**2 + (goal_location[1] - s_location[1])**2)**(1/2)

# The function returns whether n_location should be generated (checks in open_list)
# removes a node from open_list if needed
# we will check if n is in the open list
def check_for_duplicates_open(n_location, s, open_list):
    for i in range(len(open_list)):
        if open_list[i][3] == n_location[0] and open_list[i][4] == n_location[1]:
            if open_list[i][2] < s[2] + 1:
                return True
        else:
            heapq.heappop(open_list)
    return False
  
  
# The function returns whether n_location should be generated (checks in closed_list)
# removes a node from closed_list if needed  
def check_for_duplicates_close(n_location, s, closed_list):
    if n_location in closed_list:
        if closed_list[n_location][2] < s[2] + 1:
            return True
        else:
            closed_list.pop(closed_list.pop(n_location))
    return False
    
    
# Locations are tuples of (x, y)
def astar_search(grid, start_location, goal_location):
    # State = (f, h, g, x, y, s_prev) # f = g + h (For Priority Queue)
    # Start_state = (0, 0, 0, x_0, y_0, False)
    start = (0, 0, 0, start_location[0], start_location[1], False)
    open_list = init_open()
    closed_list = {}
    # Mark the source node as
    # visited and enqueue it
    insert_to_open(open_list, start)
    while len(open_list) != 0:
        # Dequeue a vertex from
        # queue and print it
        s = get_best(open_list)
        s_location = (s[3], s[4])
        if s_location in closed_list:
            continue
        if is_goal(s_location, goal_location):
            print("The number of states visited by AStar Search:", len(closed_list))
            return s
        neighbors_locations = get_neighbors(grid, s_location)
        for n_location in neighbors_locations:
            if check_for_duplicates_open(n_location, s, open_list) or check_for_duplicates_close(n_location, s, closed_list):
                continue
            h = calculate_heuristic(n_location, goal_location)
            g = s[2] + 1
            f = g + h
            n = (f, h, g, n_location[0], n_location[1], s)
            insert_to_open(open_list, n)
        closed_list[s_location] = s

def print_route(s):
    for r in s:
        print(r)

def get_route(s):
    route = []
    while s:
        s_location = (s[3], s[4])
        route.append(s_location)
        s = s[5]
    route.reverse()
    return route

def print_grid_route(route, grid):
    for location in route:
        grid[location] = 'x'
    print(pd.DataFrame(grid))


# Sean Functions
def valid_move(grid, x, y):
    row = len(grid)
    col = len(grid)
    return (0 <= x < row) and (0 <= y < col)

