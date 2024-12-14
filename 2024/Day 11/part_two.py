pebble_map : dict[int : int] = {}
new_pebble_map : dict[int : int] = {}

with open("data.txt") as file:
    data = file.read()
    data_list_str = data.split(" ")
    pebble_list = [int(x) for x in data_list_str]
    for this_pebble in pebble_list:
        if not this_pebble in pebble_map.keys():
            pebble_map[this_pebble] = 0
        pebble_map[this_pebble]+=1

def add_new_pebble(value, count):
    if not value in new_pebble_map.keys():
        new_pebble_map[value] = 0
    new_pebble_map[value] += count

MAX_BLINKING = 75
for _ in range(MAX_BLINKING):
    print(_,": ", len(pebble_map.keys()))
    new_pebble_map = {}
    for this_pebble in pebble_map.keys():
        this_count = pebble_map[this_pebble]
        # Apply the first fitting rule
        if this_pebble == 0:
            add_new_pebble(1, this_count)
            continue
        
        pebble_num_str = str(this_pebble)
        if (len(pebble_num_str) % 2) == 0:
            half_size = len(pebble_num_str) // 2
            add_new_pebble(int(pebble_num_str[:half_size]), this_count)
            add_new_pebble(int(pebble_num_str[half_size:]), this_count)
        else:
            add_new_pebble(this_pebble * 2024, this_count)
    pebble_map = new_pebble_map

total_num = 0
total_num += sum(pebble_map[x] for x in pebble_map)
print(total_num)