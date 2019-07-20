#dictionaries are an unordered set of key: value pairs

my_dict = {"item": "pen", "food": "fries", "number_brother": 1}

print(my_dict)

my_dict.update({"new_item": "pencil", "number_cousins": 2})

print(my_dict)

#list comprehensions to dicts

names = ["thales", "tylex", "carlos", "salles", "alisson"]

ages = [23, 18, 34, 56, 27]

dic = {key:value for key, value in zip(names, ages)}

print(dic)

#get allows to return value from a specific key without worrying whether key exists or not, params are key and default return value
#the same analogy goes on for a pop method

print(dic.get("thales", 0))
print(dic.pop("thalez", 99))

list_keys = dic.keys()
print(list_keys)

list_vals = dic.values()
print(list_vals)

for n, a in dic.items():
    print("{} is {} years old".format(n, a))
