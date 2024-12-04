import re

data_str = None

with open("data.txt", "r+") as file1:
    data_str = file1.read()

matches_do = re.finditer(r'do\(\)|don\'t\(\)', data_str)
delete_mode : bool = False
ignore_from = 0
write_from = 0
new_text = ""
for match in matches_do:
    if match.group() == "do()":
        if delete_mode == True:
            delete_mode = False
            write_from = match.end()

    elif match.group() == "don't()":
        if delete_mode == False:
            delete_mode = True
            ignore_from = match.end()
            # append the text
            new_text += data_str[write_from:match.start()]

if delete_mode == False:
    new_text+=data_str[write_from:-1]

print(new_text)
# We will find with regex all 
pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches_muls = re.finditer(pattern, str(new_text))

result = 0
for match in matches_muls:
    numbers = re.findall(r'\d+', match.group())
    a = int(numbers[0])
    b = int(numbers[1])
    result += a*b
print(result)