# dict1={'brand':'maruti','model':'dzire','year':2020}
# # print(dict1)

# # dict1['color']='blue'
# # print(dict1)         add any new key-value

# # print(len(dict1)) it will count pair as one

# # dict1.pop("brand")
# # print(dict1)

# # dict1.popitem()
# # print(dict1)  it will auto delete the  last element

# # dict1.clear()
# # print(dict1)  it willdelete full dict

# # x=dict1.copy()  copy the dict
# # print(x)


# # b=dict1.keys()
# # print(b)      print keys


# # b=dict1.values()  print values
# # print(b)


# # b=dict1.items()
# # print(b)   print full dict in a list

# # a=dict1.fromkeys('brand')  it will part the word in letter
# # print(a)



# #nested dict
# nested_dict = {
#     'first_level_key': {
#         'second_level_key': 'second_level_value',
#         'another_second_level_key': 'another_second_level_value'
#     },
#     'another_first_level_key': {
#         'second_level_key': 'second_level_value'
#     }
# }
# value = nested_dict['first_level_key']['second_level_key']
# print(value)  # Output: 'second_level_value'

dict1={
    "study":{"class":12,"age":18},
    "player":{"name":"virat","age":32}
}
print(dict1)
print(dict1["study"])
print(dict1["player"]["name"])
