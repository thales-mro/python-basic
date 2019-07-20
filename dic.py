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
