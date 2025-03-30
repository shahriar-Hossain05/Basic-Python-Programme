username = input("Enter a username: ")


if len(username) > 12 :
    print("Your username cant be more than 12 characters")
elif username.find(" ") != -1 :
    print("Username must not contain any spaces")
elif username.isalpha() == False :
    print("Your username must not contain digits")

else :
    print(f"Welcome {username}")
