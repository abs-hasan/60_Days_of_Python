# TODO Reading

# file using open() method
# Need to close
file = open("my_file.txt")
contents = file.read()
print(contents)
file.colse()

# file open by using with open() method.
# no need use close method.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# read file line by line
with open("my_file.txt") as file:
    data = file.readlines()
    print(data)

# print one line only . 1st line
with open("my_file.txt") as file:
    data = file.readline()
    print(data)

# Provide boolean value of readable or not
with open("my_file.txt") as file:
    data = file.readable()
    print(data)

# TODO Writing the file


# by default it is only readable
# this way all previous value will be erased
# Also will create new file if it does not exist
with open("my_files.txt", mode="w") as file:
    data = file.write("New Text line 1")
    print("w")

# to avoid above issue we will use append which is "a"
with open("my_file.txt", mode="a") as file:
    data = file.write("\nNew Text line 1")
    print("w")

with open("my_file.txt") as file:
    data = file.readlines()
    print(data)

with open("my_files.txt") as file:
    data = file.readlines()
    print(data)

#TODO Relative file and absolute file

# Absolute file start with forward slash / Its a root
# Working directory where we are currently working
# ../ to go back

with open("/Users/ABS/Desktop/my_file.txt") as file:
    data = file.read()
    print(data)

# C:\Users\ABS\PycharmProjects\readingCSVinpython

with open("../../../ABS/my_file.txt") as file:
    data = file.read()
    print(data)