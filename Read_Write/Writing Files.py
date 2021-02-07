# Writing in the files
'''
example_file = open("Example1.txt", "w")  # a -> appending, w -> Write (overwrite the existing file)
'''
# using the name of the file that doesn't exist creates a new file
# also write/create different language in python
example_file = open("index.html","w")

example_file.write("<p>This is HTML</p>")


example_file.close()
