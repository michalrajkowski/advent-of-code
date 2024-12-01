dict_1 : dict[int, int] = {}
dict_2 : dict[int, int] = {}

with open("data.txt", "r+") as file1:
    data_str = file1.readlines()
    for line in data_str:
        (a,b) =map(int, line.split())
        # insert to dicts, if there is none, set to zero in both
        if not a in dict_1:
            dict_1[a] = 0
        if not a in dict_2:
            dict_2[a] = 0
        if not b in dict_2:
            dict_2[b] = 0
        dict_1[a] +=1
        dict_2[b] +=1

similarity_score = 0
for key in dict_1.keys():
    value = dict_1[key]
    similarity_score += value*dict_2[key]*key

print(similarity_score)