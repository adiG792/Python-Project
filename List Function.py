
lucky_num = [7, 35, 5, 90, 13, 45, 12, 7]
friends = ["Pheobe", "Ross", "Joey","Chandelar", "Monica", "Rachel", "Joey"]
friends2 = friends.copy()

print(friends)
print(friends2)

#know the index of ceratin value

print(friends.index("Rachel"))

#count no. of same element

print(friends.count("Joey"))

#Arrange list

lucky_num.sort()
print(lucky_num)

#reverse list

lucky_num.reverse()
print(lucky_num)

#adding lists

friends.extend(lucky_num)
print(friends)

#add individual element of list

friends.append("Creed") #append fuction add the element only at the end of the list
print(friends)

#add individual element at any index position

friends.insert(1, "Janice") #list.insert('index no.', element)
print(friends)

#remove element from list

friends.remove("Ross") #remove a certain element
print(friends)

friends.pop() #remove last element
print(friends)

friends.clear() #remove every element
print(friends)

