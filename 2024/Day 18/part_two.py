import re

falling_rocks_positions = []
rocks_map = {}

with open("data.txt") as file:
    data_lines = file.readlines()
    for line in data_lines:
        numbers = re.findall(r'\d+', line)
        falling_rocks_positions.append((
            int(numbers[0]),
            int(numbers[1])
        ))
    
MAX_I, MAX_J = 70,70
# Create empty map
rocks_map = {(i,j):False for i in range(MAX_I+1) for j in range(MAX_J+1)}

def is_in_map(point):
    (x,y) = point
    if 0 <= x <= MAX_I and 0 <= y <= MAX_J:
        return True
    return False

# Do bfs, check after how many moves the goal can be reached
# LOOK FOR EXIT AFTER FALLING BYTES:
for i,falling_byte_coords in enumerate(falling_rocks_positions):
    print(i)
    rocks_map[falling_byte_coords] = True

    # Load initial values:
    neighbour_matrix = [(1,0),(-1,0),(0,1),(0,-1)]
    visited_map = {(i,j):0 for i in range(MAX_I+1) for j in range(MAX_J+1)}
    queue = []

    starting_point = (0,0)
    ending_point = (MAX_I, MAX_J)

    queue.append(starting_point)
    visited_map[starting_point] = 0

    while len(queue) > 0:
        this_point = queue.pop(0)

        # Rozważ sąsiadów
        for nei_mod in neighbour_matrix:
            new_point = (this_point[0]+nei_mod[0],
                        this_point[1]+nei_mod[1])
            if not is_in_map(new_point):
                continue
            if rocks_map[new_point] == True:
                continue
            if visited_map[new_point] > 0:
                continue
            
            # We can move here:
            visited_map[new_point] = visited_map[this_point]+1
            queue.append(new_point)
        if visited_map[ending_point] != 0:
            break
    if visited_map[(ending_point)] == 0:
        print(falling_byte_coords)
        break

def print_visited_map():
    map_str = ""
    for j in range(MAX_J+1):
        for i in range(MAX_I+1):
            if rocks_map[(i,j)]:
                map_str+="#"
            else:
                map_str+=str(visited_map[(i,j)])
        map_str+="\n"
    print(map_str)