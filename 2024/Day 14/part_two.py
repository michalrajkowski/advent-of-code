import re

pattern = r'-?\d+'
guard_data : list[tuple[int,int,int,int]]= []
# Get the input data
with open("data.txt") as file:
    data_lines = file.readlines()
    for line in data_lines:
        matches = re.findall(pattern, line)
        matches_int = [int(x) for x in matches]
        guard_data.append(tuple(matches_int))

MAP_X, MAP_Y = 101, 103
neighbour_mods = [(1,0),(-1,0),(0,1),(0,-1)]
def is_in_map_extended(point):
    (x,y) = point
    if -1<= x <= MAP_X and -1 <= y <= MAP_Y:
        return True
    return False

lowest_found_frame = -1
lowest_found_value = 99999999999999

for NUM_OF_SEC in range(8000, 8300):
    map_of_guards = {(x,y) : 0 for x in range(-1, MAP_X + 1) for y in range(-1, MAP_Y + 1)}
    # Calculate each guard final place:
    for guard_params in guard_data:
        (x,y,v_x,v_y) = guard_params
        final_x = (x+v_x*NUM_OF_SEC)%MAP_X
        final_y = (y+v_y*NUM_OF_SEC)%MAP_Y
        map_of_guards[(final_x, final_y)]+=1
    # Do bfs from (-1,-1) and find the percent of visited map?
    # If the christmas tree is "coherent/filled inside" shape it should dramaticly lower the result in its frame
    queue = []
    queue.append((-1,-1))
    map_of_guards[(-1,-1)] = -1
    while len(queue) > 0:
        this_point = queue.pop()
        # Check neighs
        for this_mod in neighbour_mods:
            next_point = (this_point[0]+this_mod[0], this_point[1]+this_mod[1])
            if not is_in_map_extended(next_point):
                continue
            if map_of_guards[next_point] != 0:
                continue
            map_of_guards[next_point] = -1
            queue.append(next_point)
    # now calculate the percent of -1 to the all results in dict
    count_minus_ones = list(map_of_guards.values()).count(-1)
    if lowest_found_value > count_minus_ones:
        lowest_found_value = count_minus_ones
        lowest_found_frame = NUM_OF_SEC
    print(NUM_OF_SEC, ": ", " frame: ", lowest_found_frame, " value: ", lowest_found_value)

map_of_guards = {(x,y) : 0 for x in range(-1, MAP_X + 1) for y in range(-1, MAP_Y + 1)}
for guard_params in guard_data:
        (x,y,v_x,v_y) = guard_params
        final_x = (x+v_x*lowest_found_frame)%MAP_X
        final_y = (y+v_y*lowest_found_frame)%MAP_Y
        map_of_guards[(final_x, final_y)]+=1
tree_image = ""
for j in range(MAP_Y):
    for i in range(MAP_X):
        if map_of_guards[(i,j)] == 0:
            tree_image+="."
        else:
            tree_image+="#"
    tree_image+="\n"
print(tree_image)