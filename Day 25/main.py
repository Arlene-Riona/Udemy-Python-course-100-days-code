# with open("weather_data.csv", "r") as weather_file:
#     data = weather_file.readlines()

import csv
import pandas
'''
temperatures = []
with open("weather_data.csv", "r") as weather_file:
    # returns an object that can be looped and accessed
    data = csv.reader(weather_file)
    for item in data:
        if item[1] != "temp":
            temperatures.append(int(item[1]))
print(temperatures)
'''
data = pandas.read_csv("weather_data.csv") # dataframe
# print(type(data)) # <class 'pandas.core.frame.DataFrame'>
# print(type(data["temp"])) # series

# converting the data frame to dictionary
# dictionary = data.to_dict()
# #print(dictionary)
#
# # converting the data series to lst
# lst = data["temp"].to_list()
#
# average = sum(lst)/len(lst)
# print(round(average, 2))
#
# # getting the avg
# avg = data["temp"].mean()
# print(avg)
#
# # getting the maximum value
# maximum = data["temp"].max()
# print(maximum)
#
# # getting data from a column
# print(data.temp) # same as data["temp"]

# getting the data from a row
# SYNTAX >>> print(data_frame[column == condition])
# print(data[data["day"] == "Tuesday"])

# getting the data from the row where the tem is max
max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# getting a particular value from a row
# >>> monday = dataframe[condition]
# monday = data[data.day == "Monday"]
# >>> tap into the attribute, monday.attribute or monday["attribute"]
# temp = monday.temp
# print(temp)

# converting monday's temp from C to F
# monday_temp = data[data.day == "Monday"].temp
temp = data.temp[0]
# print(monday_temp)
# print(temp)
f = (9/5) * temp + 32
print(f)

# creating a dataframe from scratch
# >>> you can have your data in any form like a dictionary
dictionary = {
    "students": ["A", "B", "C"],
    "grades": [80, 78, 100]
}
# >>> pandas.<Class "DataFrame">(your_data)
data = pandas.DataFrame(dictionary)
# converting the dataframe to csv and saving it in a file
data.to_csv("new_csv_students.csv")