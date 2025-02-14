import random
import statistics as s
import string

#1. create a list of random number of dicts (from 2 to 10)
dict_count=random.randint(2, 10)
print(dict_count)
myList=[]
for i in range(dict_count):
    dict_count_elements=random.randint(1, 10)
    key_list=[]
    value_list=[]
    for j in range(dict_count_elements):
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100)
        key_list.append(chr(random.randint(ord('a'), ord('z'))))
        value_list.append(random.randint(0, 100))
    print(key_list)
    print(value_list)
    d = {i: j for i, j in zip(key_list, value_list)}
    print(d)
    myList.append(d)
#example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
print(myList)


# Create an empty dictionary to store the combined results
combined_dict = {}

# Iterate through the list of dictionaries
for i, d in enumerate(myList, start=1):
    # Iterate through each key-value pair in the dictionary
    for key, value in d.items():
        # Construct a new key with dict number if key exists multiple
        new_key = f"{key}_{i}" if key in combined_dict else key
        # Update the combined dictionary with the maximum value for each key
        if key in combined_dict:
            combined_dict[new_key] = max(combined_dict[key], value)
            del combined_dict[key]  # Remove old key without index
        else:
            combined_dict[new_key] = value

print("Combined dictionary:", combined_dict)

