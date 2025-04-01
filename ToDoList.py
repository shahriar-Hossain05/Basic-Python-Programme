tasks = []


while True:    #starts a infinite loop
    action = input("Type 'A' to add a task and type 'Q' to quit: ")

    if action == "A":
        task = input("Enter the task you wanna complete: ")
        tasks.append(task)
    elif action == "Q":
        break
    else:
        print("Invalid options, please try again")

print("Your To-Do Lists: ")

for index, task in enumerate(tasks,start=1):
    print(f"{index}.{task}")

