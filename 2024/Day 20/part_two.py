race_map = {}
start_point, end_point = None, None
data_lines = []
with open("data.txt") as file:
    data_lines = file.readlines()
    for j, line in enumerate(data_lines):
        for i, char in enumerate(line.strip()):
            if char == "S":
                start_point = (i,j)
                race_map[(i,j)] = 0
            elif char == "E":
                end_point = (i,j)
                race_map[(i,j)] = 0
            elif char == ".":
                race_map[(i,j)] = 0
            elif char == "#":
                race_map[(i,j)] = 1

MAX_J = len(data_lines)
MAX_I = len(data_lines[0].strip())

def is_in_map(point):
    (x,y) = point
    if 0 <= x < MAX_I and 0 <= y < MAX_J:
        return True
    return False

MAX_INT = 2147483647
neighbour_matrix = [(1,0),(-1,0),(0,1),(0,-1)]

finish_to_here_seconds = {(i,j):MAX_INT for i in range (MAX_I) for j in range(MAX_J)}
queue = []
queue.append(end_point)
finish_to_here_seconds[end_point] = 0
# Start from the end and see in what time you can get to each point?
while len(queue) > 0:
    this_point = queue.pop(0)
    for nei_move in neighbour_matrix:
        new_point = (this_point[0]+nei_move[0],
                     this_point[1]+nei_move[1])
        
        if race_map[new_point] == 1:
            continue
        
        if finish_to_here_seconds[this_point]+1 < finish_to_here_seconds[new_point]:
            finish_to_here_seconds[new_point] = finish_to_here_seconds[this_point]+1
            queue.append(new_point)


print(finish_to_here_seconds[start_point])
# Then start from the "start", look where you phase doing the bfs + cheat and calculate the differnece?
how_much_cheats_that_saves_this_time = {time : 0 for time in range(finish_to_here_seconds[start_point] + 1)}
time_cheat_positions = {time : [] for time in range(finish_to_here_seconds[start_point] + 1)}
# Create all the cheetos_moves_mods
cheetos_moves_mods_set = {(0, 0)}  # Start at the origin

for _ in range(20):  # Iterate up to 20 moves
    new_positions = set()
    for pos in cheetos_moves_mods_set:
        for move in neighbour_matrix:
            new_pos = (pos[0] + move[0], pos[1] + move[1])
            new_positions.add(new_pos)
    cheetos_moves_mods_set.update(new_positions)

start_to_here_seconds = {(i,j):MAX_INT for i in range (MAX_I) for j in range(MAX_J)}
queue = []
queue.append(start_point)
start_to_here_seconds[start_point] = 0

def rasterized_shortest_line(start, end):
    """
    Computes the shortest rasterized line between two points using horizontal and vertical moves.

    :param start: Tuple (x1, y1) for the starting point
    :param end: Tuple (x2, y2) for the ending point
    :return: List of grid points along the shortest rasterized path
    """
    x1, y1 = start
    x2, y2 = end
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x_step = 1 if x2 > x1 else -1
    y_step = 1 if y2 > y1 else -1

    path = [(x1, y1)]
    error = 0  # Tracks when to alternate directions

    # Bresenham-like rasterized line
    while (x1, y1) != (x2, y2):
        if (error + dy) < dx:
            x1 += x_step
            error += dy
        else:
            y1 += y_step
            error -= dx
        path.append((x1, y1))

    return path

visited_pair = set()

while len(queue) > 0:
    this_point = queue.pop(0)

    # For this move try all the cheetos jumps:
    for cheetos_mod in cheetos_moves_mods_set:
        cheat_point = (this_point[0]+cheetos_mod[0],
                       this_point[1]+cheetos_mod[1])
        if not is_in_map(cheat_point):
            continue
        if finish_to_here_seconds[cheat_point] == MAX_INT:
            continue
        # Shoot line and find the first wall position, before wall position, last wall pos and first after_wall pos?
        cheat_len = abs(cheetos_mod[0]) + abs(cheetos_mod[1])
        if cheat_len < 2:
            continue
        # Shoot line:
        move_line = rasterized_shortest_line(this_point, cheat_point)
        # print(move_line)
        # Find first wall, last wall, first "before wall" point, first "after wall" point
        first_before_wall = None
        first_after_wall = None
        # before wall:
        for index, line_point in enumerate(move_line):
            if race_map[line_point] == 1:
                first_before_wall = move_line[index-1]
                first_wall = move_line[index]
                break
        # after wall:
        for index, line_point in enumerate(move_line):
            if race_map[line_point] == 1:
                next_line_point = move_line[index+1]
                if race_map[next_line_point] == 0:
                    first_after_wall = next_line_point
        if this_point == (1,3) and cheat_point == (5,7):
            print(move_line)
            print(first_before_wall)
            print(first_after_wall)

        
        if first_after_wall == None or first_before_wall == None:
            continue

        # Check if this pair is in set
        if (first_before_wall,first_after_wall) in visited_pair:
            continue

        if start_to_here_seconds[first_before_wall] == MAX_INT:
            continue
        if finish_to_here_seconds[first_after_wall] == MAX_INT:
            continue

        line_shortcut_len = abs(first_before_wall[0] - first_after_wall[0]) + abs(first_before_wall[1] - first_after_wall[1])
        normaly_from_start = finish_to_here_seconds[start_point] - finish_to_here_seconds[first_after_wall]
        from_start_with_cheats = line_shortcut_len + start_to_here_seconds[first_before_wall]
        time_saved = normaly_from_start - from_start_with_cheats
        if time_saved > 0:
            how_much_cheats_that_saves_this_time[time_saved]+=1
            time_cheat_positions[time_saved].append((first_before_wall, first_after_wall))
            visited_pair.add((first_before_wall,first_after_wall))

    for nei_move in neighbour_matrix:
        new_point = (this_point[0]+nei_move[0],
                     this_point[1]+nei_move[1])
        
        if race_map[new_point] == 1:
            continue
        
        if start_to_here_seconds[this_point]+1 < start_to_here_seconds[new_point]:
            start_to_here_seconds[new_point] = start_to_here_seconds[this_point]+1
            queue.append(new_point)

how_many_100_plus_sec = 0
for i in range(start_to_here_seconds[end_point]):
    if how_much_cheats_that_saves_this_time[i] > 0:
        print(i,":",how_much_cheats_that_saves_this_time[i])
        #if i < 100:
        #    continue
        #how_many_100_plus_sec+=how_much_cheats_that_saves_this_time[i]
print(how_many_100_plus_sec)
print(time_cheat_positions[76])