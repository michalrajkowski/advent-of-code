robot_moves_list : list[tuple[int,int]] = []
robot_map : dict[tuple[int,int] : int] = {}
map_data_str : list[str] = []
moves_data_str : list[str] = []
player_pos : tuple[int,int] = None
# Get the input data
# Read the map data
# if empty line found
# read the moves data
int_to_char_map = {
    0:'.',
    1:'#',
    2:'[',
    3:']'
}

def visualise_map():
    map_str = ""
    for j in range(len(map_data_str)):
        for i in range(2*len(map_data_str[0])-2):
            char_int = robot_map[(i,j)]
            char_str = int_to_char_map[char_int]
            map_str+=char_str
        map_str+="\n"
    print(map_str)


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
            player_pos = (2*i,j)
            robot_map[(2*i,j)] = 0 
            robot_map[(2*i+1,j)] = 0    
        elif char == '#':
            robot_map[(2*i,j)] = 1
            robot_map[(2*i+1,j)] = 1
        elif char == '.':
            robot_map[(2*i,j)] = 0
            robot_map[(2*i+1,j)] = 0
        elif char == 'O':
            robot_map[(2*i,j)] = 2
            robot_map[(2*i+1,j)] = 3

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

visualise_map()
MAX_J = len(map_data_str)
MAX_I = 2*len(map_data_str[0])-2

# Method to get the second element of a box:
def get_friend_pos(part_pos):
    if robot_map[part_pos] == 2:
        # It is to the right
        return (part_pos[0]+1, part_pos[1])
    # It is to the left
    return (part_pos[0]-1, part_pos[1])

def can_push_horizontal(start_point, push_dir):
    this_point = start_point
    remembered_parts : list[tuple[tuple[int,int],int]]= []

    while(robot_map[this_point] != 1):
        if robot_map[this_point] >= 2:
            remembered_parts.append((this_point,robot_map[this_point]))
            friend_pos = get_friend_pos(this_point)
            remembered_parts.append((friend_pos,robot_map[friend_pos]))
        if robot_map[this_point] == 0:
            # We can push!
            # Actualy move all the boxes:
            for element in remembered_parts:
                pos, id = element
                robot_map[pos] = 0
            for element in remembered_parts:
                pos, id = element
                new_pos = (pos[0]+push_dir[0], pos[1])
                robot_map[new_pos] = id
            return True
        this_point = (this_point[0]+2*push_dir[0], this_point[1])
    return False

# Check all above positions to the things that needs to be pushed
# - if wall - the end
# - if 
def can_push_vertical(start_point, push_dir):
    positions_now_pushed = set()
    this_point = start_point
    remembered_parts : list[tuple[tuple[int,int],int]]= []
    
    positions_now_pushed.add(start_point)
    positions_now_pushed.add(get_friend_pos(start_point))


    while True:
        new_to_push = set()
        # Check all the positions above those in set
        for pos in positions_now_pushed:
            above_position = (pos[0]+push_dir[0], pos[1]+push_dir[1])
            if robot_map[above_position] == 1:
                return False
            #if robot_map[above_position] == 0:
                # its ok?
            if robot_map[above_position] >= 2:
                # Add to new_to_push pos and his frined
                new_to_push.add(above_position)
                new_to_push.add(get_friend_pos(above_position))
        
        # Save checked elements for later map modifications
        for pos in positions_now_pushed:
            remembered_parts.append((pos, robot_map[pos]))
        
        if len(new_to_push) == 0:
            # All is good, we can start moving
            for element in remembered_parts:
                pos, id = element
                robot_map[pos] = 0
            for element in remembered_parts:
                pos, id = element
                new_pos = (pos[0]+push_dir[0], pos[1]+push_dir[1])
                robot_map[new_pos] = id
            return True
        else:
            positions_now_pushed=new_to_push
        

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
    if robot_map[new_point] >= 2:
        # Different handling for horizontal and vertical push
        if move_mod[0] != 0:
            if can_push_horizontal(new_point, move_mod):
                player_pos = new_point
                continue
        else:
            if can_push_vertical(new_point, move_mod):
                player_pos = new_point
                continue
        
visualise_map()

# Calculate the GPS:
gps_total = 0
for key in robot_map.keys():
    if robot_map[key] != 2:
        continue
    # find the closest x and y
    x1 = key[0]
    # x2 = MAX_I-key[0]-2
    x2 = x1
    x = min(x1,x2)
    y1 = key[1]
    # y2 = MAX_J-key[1]-1
    y2 = y1
    y = min(y1,y2)
    gps_total+= x + 100*y
print(gps_total)