dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# In-place
dict1.update(dict2)
print(dict1)

# New dict
merged_dict = dict1 | dict2
print(merged_dict)