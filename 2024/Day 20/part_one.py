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

# Create all the cheetos_moves_mods
cheetos_moves_mods_set = set()
for m1 in neighbour_matrix:
    for m2 in neighbour_matrix:
        new_mod = (m1[0] + m2[0],
                   m1[1] + m2[1])
        # Check if distance is 2
        if abs(new_mod[0]) + abs(new_mod[1]) == 2:
            cheetos_moves_mods_set.add(new_mod)

start_to_here_seconds = {(i,j):MAX_INT for i in range (MAX_I) for j in range(MAX_J)}
queue = []
queue.append(start_point)
start_to_here_seconds[start_point] = 0

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
        normaly_from_start = finish_to_here_seconds[start_point] - finish_to_here_seconds[cheat_point]
        from_start_with_cheats = 2 + start_to_here_seconds[this_point]
        time_saved = normaly_from_start - from_start_with_cheats
        if time_saved > 0:
            how_much_cheats_that_saves_this_time[time_saved]+=1

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
        if i < 100:
            continue
        how_many_100_plus_sec+=how_much_cheats_that_saves_this_time[i]
print(how_many_100_plus_sec)