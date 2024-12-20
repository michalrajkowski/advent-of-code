# SUPER COMPUTER
import re
import operator
import copy

pattern_number = r'\d+'

registers : dict[int:int]= {}
program_insructions = []

with open("data.txt") as file:
    data_lines = file.readlines()
    # Read registers data
    for i in range(3):
        numbers = re.findall(r'\d+', data_lines[i])
        registers[i] = int(numbers[0])
    # Read instructions line 
    numbers = re.findall(r'\d+', data_lines[4])
    program_insructions = [int(n_str) for n_str in numbers]

def get_combo_value(number):
    if number <= 3:
        return number
    if number < 7:
        return registers[number - 4]

A = 37221261688308
looking_for_num_on_index = 12

while True:
    registers[0] = A
    registers[1] = 0
    registers[2] = 0
# Run program:
    i = 0
    output_feed = []
    while i < len(program_insructions):
        # Read the instruction at index
        # Based on instruction type, increase the index
        this_instruction_num = program_insructions[i]
        match this_instruction_num:
            case 0: # adv
                instruction_input = program_insructions[i+1]
                i+=2

                numerator = registers[0]
                denominator = 2**get_combo_value(instruction_input)
                fraction = numerator // denominator
                registers[0] = fraction
            case 1: # bxl
                instruction_input = program_insructions[i+1]
                i+=2

                x1 = registers[1]
                x2 = instruction_input
                result = operator.xor(x1, x2)
                registers[1] = result
            case 2: # bst
                instruction_input = program_insructions[i+1]
                i+=2

                result = get_combo_value(instruction_input)%8
                registers[1] = result
            case 3: # jnz
                instruction_input = program_insructions[i+1]
                i+=2

                if registers[0] != 0:
                    i = instruction_input
            case 4: # bxc
                instruction_input = program_insructions[i+1]
                i+=2
                
                x1 = registers[1]
                x2 = registers[2]
                result = operator.xor(x1,x2)
                registers[1] = result
            case 5: # out
                instruction_input = program_insructions[i+1]
                i+=2

                result = get_combo_value(instruction_input)%8
                # Output the result
                output_feed.append(result)
            case 6: # bdv
                instruction_input = program_insructions[i+1]
                i+=2
                
                numerator = registers[0]
                denominator = 2**get_combo_value(instruction_input)
                fraction = numerator // denominator
                registers[1] = fraction
            case 7: # cdv
                instruction_input = program_insructions[i+1]
                i+=2
                
                numerator = registers[0]
                denominator = 2**get_combo_value(instruction_input)
                fraction = numerator // denominator
                registers[2] = fraction
    # check if we found the number
    sublist = program_insructions[-1:-1*looking_for_num_on_index-2:-1]
    if tuple(sublist[::-1]) == tuple(output_feed):
        print(A)
        A*=8
        looking_for_num_on_index+=1
    A+=1

    