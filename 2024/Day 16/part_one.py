import sys

MAX_INT = 9223372036854775807
raindeer_map = {}
start_point = None
end_point = None
visited_map : dict[tuple[tuple[int, int], tuple[int, int]] : int] = {} # dict of tuples containing
#points and raindeer direction, inside each it is stored the current lowest cost to get here

with open("data.txt") as file:
    data_lines = file.readlines()
    for j, line in enumerate(data_lines):
        for i, char in enumerate(line.strip()):
            if char == "#":
                raindeer_map[(i,j)] = 1
            else:
                raindeer_map[(i,j)] = 0
            if char == "S":
                start_point = (i,j)
            elif char == "E":
                end_point = (i,j)

directions = [(1,0),(-1,0),(0,1),(0,-1)]

for key in raindeer_map.keys():
    for dir in directions:
        visited_map[(key,dir)] = MAX_INT

def calculate_rotate_cost(this_dir, new_dir):
    _directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Find the indices of the current and new direction in the directions list
    this_index = _directions.index(this_dir)
    new_index = _directions.index(new_dir)

    # Calculate the absolute difference in indices
    diff = abs(this_index - new_index)

    # The cost is the minimum of the direct difference or wrapping around
    return min(diff, 4 - diff) * 1000

    

queue = []
queue.append((start_point, (1,0)))
visited_map[(start_point, (1,0))] = 0

while len(queue) > 0:
    (this_point, this_dir) = queue.pop()
    # Try to move and try all rotations
    # add all that were possible to queue
    # remember to increase lengths accordingly
    # avoid walls when moving

    for dir in directions:
        rotate_cost = calculate_rotate_cost(this_dir, dir)
        new_cost = rotate_cost + visited_map[(this_point, this_dir)]
        if new_cost < visited_map[(this_point, dir)]:
            visited_map[(this_point, dir)] = new_cost
            queue.append((this_point, dir))

    # Try move:
    new_point = (this_point[0]+this_dir[0], this_point[1]+this_dir[1])
    if raindeer_map[new_point] == 1:
        continue
    new_cost = visited_map[(this_point, this_dir)] + 1
    if new_cost < visited_map[(new_point, this_dir)]:
        visited_map[(new_point, this_dir)] = new_cost
        queue.append((new_point, this_dir))

# Find the lowest point in the exit:
min_result = MAX_INT
for dir in directions:
    new_result = visited_map[(end_point,dir)]
    min_result = min(min_result, new_result)
print(min_result)