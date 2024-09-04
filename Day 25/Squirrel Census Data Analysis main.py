import pandas

# pandas reads it into memory using the read_csv() function, which returns a pandas dataframe.
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240807.csv")
fur_column = squirrel_data["Primary Fur Color"]
fur_column_unique_values = fur_column.unique()

all_furs_lst = []
fur_count_lst = []

for index in range(1, len(fur_column_unique_values)):
    fur_colour = fur_column_unique_values[index]
    # all fur colours are appended into a lst
    all_furs_lst.append(fur_colour)
    fur_type_count = fur_column.value_counts()[fur_colour]
    # the total num for each fur colour is appended
    fur_count_lst.append(fur_type_count)

data_dictionary = {
    "Fur Colour": all_furs_lst,
    "Count": fur_count_lst
}

data = pandas.DataFrame(data_dictionary)
print(data)
data.to_csv("squirrel_count.csv")

'''
>>> if we use the below dictionary, the numbers are in numpy values that need to be converted into python 
>>> values so either we convert the nums into python using .item() or while creating the dataframe, we
>>> pass the index by mentioning """data = pandas.DataFrame(data_dictionary, index=[0])"""

# NumPy values need to be converted to native Python type using .item()
    count_in_python = fur_type_count.item()
    
for key in range(len(all_furs_lst)):
    data_dictionary[all_furs_lst[key]] = fur_count_lst[key]
print(data_dictionary)
    
data = pandas.DataFrame(data_dictionary, index=[0])
print(data)
data.to_csv("squirrel_count.csv")
'''