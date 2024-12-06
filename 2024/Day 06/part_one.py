visited : dict[tuple[int,int] : bool] = {}
guard_map : dict[tuple[int,int] : bool] = {}
player_pos : tuple[int, int] = None
player_move_dir_list = [(0,-1),(1,0),(0, 1),(-1, 0)] # UP, RIGHT, DOWN, LEFT
player_move_dir_index = 0
data_str = None
# READ DATA
with open("data.txt", "r+") as file1:
    data_str = file1.readlines()
    for j, line in enumerate(data_str):
        for i, character in enumerate(line.strip()):
            visited[(i,j)] = False
            if character == ".":
                guard_map[(i,j)] = False
            elif character == "#":
                guard_map[(i,j)] = True
            elif character == "^":
                guard_map[(i,j)] = False
                player_pos = (i,j)

MAX_J = len(data_str)
MAX_I = len(data_str[0].strip())

def out_of_map(point : tuple[int,int]):
    x,y = point
    if  MAX_I <= x or x < 0 or MAX_J <= y or y < 0:
        return True
    return False


# Test player movement
while True:
# Simulate player walk
# Start in 
# Test player move:
# - based on player pos and dir
# - if end of map - end movement
# - if obstacle - change direction, continu
# - if empty - move + set visited
    # Mark current as visited
    # print(player_pos)
    visited[player_pos] = True
    mod_x, mod_y = player_move_dir_list[player_move_dir_index]
    next_pos = (player_pos[0]+mod_x, player_pos[1]+mod_y)
    if out_of_map(next_pos):
        break

    if guard_map[next_pos] == True: # This is wall
        # rotate player move
        player_move_dir_index+=1
        player_move_dir_index%=4
        continue

    if guard_map[next_pos] == False: # This is open spot
        # Move player
        player_pos = next_pos
        continue

sum_moves = 0
for val in visited.values():
    if val == True:
        sum_moves+=1
print(sum_moves)
