# Numbers in list can't be after number in key in instruction set
forbiden_after : dict[int, list[int]] = {key: [] for key in range(100)}
all_instruction_lists : list[list[int]]= []
with open("data.txt", "r+") as file1:
    is_first_imput_data_part : bool = True
    data_lines = file1.readlines()
    for line in data_lines:
        if line.strip() == "":
            # We found the empty line, switch mode to second
            is_first_imput_data_part = False
            continue
        if is_first_imput_data_part:
            # load condition line
            condition_numbers_str = line.strip().split("|")
            a, b = int(condition_numbers_str[0]), int(condition_numbers_str[1])
            forbiden_after[b].append(a)
            continue
        # load data lines
        instruction_list_str = line.strip().split(",")
        this_instruction_list = [int(x) for x in instruction_list_str if x.strip()]        
        all_instruction_lists.append(this_instruction_list)

middle_sum : int = 0
# Check the correctness of all lists
for this_list in all_instruction_lists:
    # For each element check if there exists element after it breaking the forbiden_after rule
    is_rule_not_broken = True
    for i in range(len(this_list)):
        # check all elements after x are fine
        x = this_list[i]
        for j in range(i+1, len(this_list)):
            y = this_list[j]
            if not y in forbiden_after[x]:
                continue
            # RULE HAS BEEN BROKEN!!!
            is_rule_not_broken = False
            break
        if not is_rule_not_broken:
            break
    if is_rule_not_broken:
        # Add to score the middle element from list
        middle_index = len(this_list) // 2
        middle_element = this_list[middle_index]
        middle_sum += middle_element
print(middle_sum)