from Word_Dictionary import DicT

s1 = DicT("Word", "Meaning")
run = True

while run:
    print("\n~Menu: \nNew Word(1), Find(2), Remove(3), PrintAll(4), Exit(5) : ")
    choice = int(input("\n\nEnter your choice: "))
    print("_________________________________________________________")
    if choice == 1:
        flag = True
        print("\n! New Word ! : \nAdd(1), Back(2) :\n\nChoose: ")
        enter = int(input())
        if enter != 2:
            while flag:
                s1.new()
                print("\n")

    elif choice == 2:
        flag = True
        print("\n! Find ! : \nSearch(1), Back(2) :\n\nChoose: ")
        enter = int(input())
        if enter != 2:
            while flag:
                search = input("Enter the word to Find: ")
                s1.word(search)
                print("\n")
    elif choice == 3:
        word = input("Enter the word to Remove: ")
        s1.remove(word)
        print("\n")
        break
    elif choice == 4:
        print("Your Dictionary: \n")
        print(s1)
        break
    else:
        s1.file.close()
        s1.inventory.close()
        run = False
    print("_________________________________________________________")
