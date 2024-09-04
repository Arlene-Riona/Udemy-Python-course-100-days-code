import pandas

dictionary = {
    "students": ["lily", "jones", "Mutty"],
    "scores": [60, 67, 100]
}

dict_data_frame = pandas.DataFrame(dictionary)
# looping through columns
# for k,v in dict_data_frame.items():
#     print(k)
#     print(v)

# looping through rows
for index, row in dict_data_frame.iterrows():
    print(index)
    print(row.scores)