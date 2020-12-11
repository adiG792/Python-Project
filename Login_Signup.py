print("Sign up\n")
user_n1 = input("Enter username: ")
pass_1 = input("Password: ")
print()
print("Login\n")
user_n = input("Enter Login credentials: ")
if user_n == user_n1:
    pass_ = input("Enter Password: ")
    while user_n == user_n1:
        if pass_ == pass_1:
            print(f"Access Granted, Welcome {user_n}")
            break

        else:
            print("Incorrect Password !")
            pass_ = input("Enter Password again: ")

else:
    print("Incorrect username !")
    while user_n != user_n1:
        user_n = input("Enter username again: ")
    pass_ = input("Enter Password: ")
    if pass_ == pass_1:
        print(f"Access Granted, Welcome {user_n}")
    while pass_ != pass_1:
        print("Incorrect Password !")
        pass_ = input("Enter Password again: ")
    if pass_ == pass_1:
        print(f"Access Granted, Welcome {user_n}")