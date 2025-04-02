import getpass
name = ''
password = ''
while not name:
    name = input("Enter your username: ")
    if not name:
        print("Please enter your username")

while not password:
    password = getpass.getpass("Enter your password: ")
    if not password:
        print("Please enter your password")

print(f"Username: {name}")
print(f"Password: {password}")
