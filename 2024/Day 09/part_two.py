disc_representation : list[(int, int)] = []

disk_encoded : str = ""
with open("data.txt") as file:
    data = file.read()
disk_encoded = data.strip()

def calculate_checksum():
    pass

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
max_id = current_id - 1
this_disc_id = max_id
while(True):
    if this_disc_id < 0:
        break
    
    index = next((i for i, (disc_id, _) in enumerate(disc_representation) if disc_id == this_disc_id), None)
    (disc_id, disc_size) = disc_representation[index]
    
    for empty_space_index, empty_space_part in enumerate(disc_representation):
        if  empty_space_part[0] != -1:
            continue
        if empty_space_index >= index:
            break
        (empty_id, empty_size) = empty_space_part
        if empty_size < disc_size:
            continue
        
        if disc_size == empty_size:
            
            disc_representation.pop(index)
            disc_representation.insert(index, (-1, disc_size))
            disc_representation.pop(empty_space_index)
            disc_representation.insert(empty_space_index, (disc_id, disc_size))
        else:
            disc_representation.pop(index)
            disc_representation.insert(index, (-1, disc_size))
            disc_representation.pop(empty_space_index)
            disc_representation.insert(empty_space_index, (-1, empty_size - disc_size))    
            disc_representation.insert(empty_space_index, (disc_id, disc_size))    
        break 
    this_disc_id -= 1
total_sum = 0
current_index = 0
for disc_fragment in disc_representation:
    (disc_id, disc_len) = disc_fragment
    if disc_id == -1:
        disc_id = 0
    range_sum = 0 
    range_sum = (((current_index + current_index + disc_len-1)*disc_len) / 2)*disc_id
    total_sum+=range_sum
    current_index+=disc_len
print(total_sum)
