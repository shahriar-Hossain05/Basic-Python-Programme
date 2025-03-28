a = float(input("a =: "))
opt = input("Choose an operation(+,-,*,/): ")
b = float(input("b =: "))

if opt == "+":
    print(a + b)
elif opt == "-":
    print(a - b)
elif opt == "*":
    print(a * b)
elif opt == "/":
    if b != 0 :
        print(a / b)
    else:
        print("ERROR")
else :
    print("Invalid operation!! Please choose +,-,*,/")