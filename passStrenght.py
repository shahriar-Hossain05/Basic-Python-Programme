key = input('Enter Password: ')

if len(key) < 6 :
    print("Weak password")
elif key.isdigit() or key.isalpha():
    print("Medium password")
else :
    print("Strong password")