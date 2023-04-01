import json

# Load the JSON file as a list
with open('extracted_good_file.json', 'r') as f:
    json_list = json.load(f)

final_dict_good = {}
for x in range(len(json_list)):
    #print(len(json_list[x]))
    key = json_list[x][0]
    value =  json_list[x][1]
    if key not in final_dict_good:
        final_dict_good[key] = value

with open("good_file.json", "w") as f:
    json.dump(final_dict_good, f)

