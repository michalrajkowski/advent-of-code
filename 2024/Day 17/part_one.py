# SUPER COMPUTER
import re
import operator

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
print(registers)
print(program_insructions)

def get_combo_value(number):
    if number <= 3:
        return number
    if number < 7:
        return registers[number - 4]

# Run program:
i = 0
output_feed = ""
while i < len(program_insructions):
    print("i:",i)
    # Read the instruction at index
    # Based on instruction type, increase the index
    this_instruction_num = program_insructions[i]
    match this_instruction_num:
        case 0: # adv
            print("adv")
            instruction_input = program_insructions[i+1]
            i+=2

            numerator = registers[0]
            denominator = 2**get_combo_value(instruction_input)
            print(denominator)
            fraction = numerator // denominator
            registers[0] = fraction
        case 1: # bxl
            print("bxl")
            instruction_input = program_insructions[i+1]
            i+=2

            x1 = registers[1]
            x2 = instruction_input
            result = operator.xor(x1, x2)
            registers[1] = result
        case 2: # bst
            print("bst")
            instruction_input = program_insructions[i+1]
            i+=2

            result = get_combo_value(instruction_input)%8
            registers[1] = result
        case 3: # jnz
            print("jnz")
            instruction_input = program_insructions[i+1]
            i+=2

            if registers[0] != 0:
                i = instruction_input
        case 4: # bxc
            print("bxc")
            instruction_input = program_insructions[i+1]
            i+=2
            
            x1 = registers[1]
            x2 = registers[2]
            result = operator.xor(x1,x2)
            registers[1] = result
        case 5: # out
            print("out")
            instruction_input = program_insructions[i+1]
            i+=2

            result = get_combo_value(instruction_input)%8
            # Output the result
            output_feed+=str(result) + ","
        case 6: # bdv
            print("bdv")
            instruction_input = program_insructions[i+1]
            i+=2
            
            numerator = registers[0]
            denominator = 2**get_combo_value(instruction_input)
            print(denominator)
            fraction = numerator // denominator
            registers[1] = fraction
        case 7: # cdv
            print("cdv")
            instruction_input = program_insructions[i+1]
            i+=2
            
            numerator = registers[0]
            denominator = 2**get_combo_value(instruction_input)
            print(denominator)
            fraction = numerator // denominator
            registers[2] = fraction
    print(registers)
print(output_feed)