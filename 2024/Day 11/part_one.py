pebble_list : list[int] = []
new_pebble_list : list[int] = []

with open("data.txt") as file:
    data = file.read()
    data_list_str = data.split(" ")
    pebble_list = [int(x) for x in data_list_str]

# Do the blinking based on rules
MAX_BLINKING = 25
for _ in range(MAX_BLINKING):
    new_pebble_list = []
    for pebble_num in pebble_list:
        # Apply the first fitting rule
        if pebble_num == 0:
            new_pebble_list.append(1)
            continue
        
        pebble_num_str = str(pebble_num)
        if (len(pebble_num_str) % 2) == 0:
            half_size = len(pebble_num_str) // 2
            new_pebble_list.append(int(pebble_num_str[:half_size]))
            new_pebble_list.append(int(pebble_num_str[half_size:]))
        else:
            new_pebble_list.append(pebble_num * 2024)
    pebble_list = new_pebble_list

print(len(pebble_list))