# with open("C:\\Users\\arlen\\OneDrive\\Desktop\\text.txt", mode="r") as file:
# in python the / or \ won't make a difference, it's understood either ways
# with open("/Users/arlen/OneDrive/Desktop/text.txt", mode="r") as file:

# working directory is: C:\Users\arlen\PycharmProjects\pythonProject demo
# \Python 100 days code all projects with pycharm\Day 24
with open("../../../../OneDrive/Desktop/text.txt", mode="r") as file:
    data = file.read()
    print(data)