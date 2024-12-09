disc_representation : list[(int, int)] = []
disk_encoded : str = ""
with open("data.txt") as file:
    data = file.read()
disk_encoded = data.strip()

current_id = 0
for i, char in enumerate(disk_encoded):
    fragment_len = int(char)
    if fragment_len == 0: 
        continue
    fragment = (-1, fragment_len)
    if i%2 == 0:
        fragment = (current_id, fragment_len)
        current_id+=1
    disc_representation.append(fragment)
while(True):
    last_disc_representation = disc_representation.pop()
    (disc_id, disc_size) = last_disc_representation
    if disc_id == -1:
        continue
    empty_space_index, empty_space_length = None, None
    for index, disc_fragment in enumerate(disc_representation):
        if disc_fragment[0] != -1:
            continue
        empty_space_index = index
        empty_space_length = disc_fragment[1]
        break
    
    if empty_space_index == None:
        disc_representation.append(last_disc_representation)
        break    
    
    if disc_size == empty_space_length:
        disc_representation.pop(empty_space_index)
        disc_representation.insert(empty_space_index, (disc_id, disc_size))
    elif disc_size > empty_space_length:
        how_much_to_move = empty_space_length
        disc_representation.pop(empty_space_index)
        disc_representation.insert(empty_space_index, (disc_id, how_much_to_move))
        disc_representation.append((disc_id, disc_size - how_much_to_move))
    else:
        how_much_to_move = disc_size
        disc_representation.pop(empty_space_index)
        disc_representation.insert(empty_space_index, (-1, empty_space_length - how_much_to_move))
        disc_representation.insert(empty_space_index, (disc_id, how_much_to_move))
total_sum = 0
current_index = 0
for disc_fragment in disc_representation:
    (disc_id, disc_len) = disc_fragment
    range_sum = 0
    range_sum = (((current_index + current_index + disc_len-1)*disc_len) / 2)*disc_id
    total_sum+=range_sum
    current_index+=disc_len
print(total_sum)
    
    
