import re

data_str = None

with open("data.txt", "r+") as file1:
    data_str = file1.read()

# We will find with regex all 
pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(pattern, data_str)

result = 0
for match in matches:
    numbers = re.findall(r'\d+', match)
    a = int(numbers[0])
    b = int(numbers[1])
    result += a*b
print(result)
