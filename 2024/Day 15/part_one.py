robot_moves_list : list[tuple[int,int]] = []
robot_map : dict[tuple[int,int] : int] = {}
map_data_str : list[str] = []
moves_data_str : list[str] = []
player_pos : tuple[int,int] = None
# Get the input data
# Read the map data
# if empty line found
# read the moves data
reading_map_data = True
with open("data.txt") as file:
    data_lines = file.readlines()
    for line in data_lines:
        if line.strip() == "":
            reading_map_data = False
            continue
        if reading_map_data:
            map_data_str.append(line)
            continue
        # Read moves data
        moves_data_str.append(line)

# Process map data
for j, line in enumerate(map_data_str):
    for i, char in enumerate(line.strip()):
        number_to_paste = 0
        if char == '@':
            player_pos = (i,j)
        elif char == '#':
            number_to_paste = 1
        elif char == 'O':
            number_to_paste = 2
        robot_map[(i,j)] = number_to_paste

moves_to_directions_dict = {
    ">":(1,0),
    "<":(-1,0),
    "^":(0,-1),
    "v":(0,1),
}
# Process moves data
for line in moves_data_str:
    for char in line.strip():
        move_mod = moves_to_directions_dict[char]
        robot_moves_list.append(move_mod)

def can_push(start_point, push_dir):
    this_point = start_point
    while(robot_map[this_point] != 1):
        if robot_map[this_point] == 0:
            # We can push!
            robot_map[this_point] = 2
            robot_map[start_point] = 0
            return True
        this_point = (this_point[0]+push_dir[0], this_point[1]+push_dir[1])
    return False

# Simulate moves:
for move_mod in robot_moves_list:
    # Try to move there
    # if it is empty slot: easy
    new_point = (player_pos[0]+move_mod[0],player_pos[1]+move_mod[1])
    # WALL
    if robot_map[new_point] == 1:
        continue
    # EMPTY SLOT
    if robot_map[new_point] == 0:
        player_pos = new_point
        continue
    if robot_map[new_point] == 2:
        if can_push(new_point, move_mod):
            player_pos = new_point
            continue

map_str = ""

# Calculate the GPS:
gps_total = 0
for key in robot_map.keys():
    if robot_map[key] != 2:
        continue
    gps_total+= key[0] + 100*key[1]
print(gps_total)