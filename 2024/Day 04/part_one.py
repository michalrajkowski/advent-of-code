def char_to_int(char : str) -> int:
    char_to_int_dict = {
        "." : -1,
        "X" : 0,
        "M" : 1,
        "A" : 2,
        "S" : 3,
    }
    return char_to_int_dict[char]

xmas_map : dict[tuple[int,int], int]  = {}
visited_map : dict[tuple[int,int], bool]  = {}
data_lines = None

with open("data.txt", "r+") as file1:
    data_lines = file1.readlines()
    for j, line in enumerate(data_lines):
        for i, char in enumerate(line.strip()):
            xmas_map[(i,j)] = char_to_int(char)
            visited_map[(i,j)] = False

xmas_count = 0

MAX_J = len(data_lines)
MAX_I = len(data_lines[0].strip())
MAX_XMAS_VALUE = 3

def point_in_map(this_point : tuple[int,int]) -> bool:
    if 0 <= this_point[0] < MAX_I and 0 <= this_point[1] < MAX_J:
        return True
    return False

def search_xmas(this_point : tuple[int,int], direction : tuple[int,int]):
    """
    Search the xmas_map in pseudo-dfs style. When you find "xmas" world -> go 
    """
    # Take neighbours
    # neighbor_array = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
    neighbor_array = [direction]
    for nei_mod in neighbor_array:
        new_point = (this_point[0]+nei_mod[0], this_point[1]+nei_mod[1])
        if not point_in_map(new_point):
            continue
        if xmas_map[new_point] != xmas_map[this_point] + 1:
            continue
        if xmas_map[new_point] == MAX_XMAS_VALUE:
            global xmas_count
            xmas_count+=1
            continue
        search_xmas(new_point, direction)

neighbor_array_moves = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
for i in range(0, MAX_I):
    for j in range(0, MAX_J):
        if xmas_map[(i,j)] == 0:
            for nei in neighbor_array_moves:
                search_xmas((i,j), nei)

print(xmas_count)

