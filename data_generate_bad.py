import json

num_blocks = 3000

with open('orig.bad.json', "r") as f:
    data = json.load(f)

print(type(data))

first_3000 = list(data.items())[:3000]
# code_blocks = []
# for item in data:
#     if len(code_blocks) >= num_blocks:
#         break
#     if 'code' in item:
#         code_blocks.append(item['code'])

with open('extracted_bad_file.json', 'w') as f:
    json.dump(first_3000, f)

print("all done")