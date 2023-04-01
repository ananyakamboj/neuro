import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y.items())
# # convert the dictionary to a list of tuples and slice the list to get the first 2 elements
first_two = list(y.items())[:2]

# # print the result
print(first_two)