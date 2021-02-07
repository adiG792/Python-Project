
friends = ["Pheobe", "Ross", "Joey", "Monica", "Rachel"]
print(friends)
#indexing from front start with 0....

print(friends[0])

#indexing with -ve value give you the value from back of list
#indexing from back start with -1....

print(friends[-2])

#select more than 1 value from lists

print(friends[1:3]) #it does not incude the last index's value

#select the whole lists from a specific index

print(friends[2:])

#modify a certain element in list

friends[1] = "Mike"
print(friends)

