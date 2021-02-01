# Reading Files from different location

# open( "file location", "r/w/a/r+" -> read/write/append/read & write)
# file location -> if same directory write only name
# otherwise -> write complete location

example_file = open("Example.txt", "r")

# check whether the file is readable or not (True only if command is read(r) or read & write(r+)
print(example_file.readable(), "\n")    # boolean value


# printing whole file
'''
print(example_file.read(), "\n")
'''

# short program
for line in example_file.readlines():
    print(line)

# print line by line
'''
print(example_file.readline())    # reads first line
print(example_file.readline())    # reads second line
'''
# or
'''
print(example_file.readlines()[2])   # puts every line an array

# remember once a line is read it is overwritten by the preceding line
# hence indexing changes accordingly
# example, ( 3 lines -> line 2 executed -> now only 2 lines left in the file)
'''

# remember to always close file after opening

example_file.close()
