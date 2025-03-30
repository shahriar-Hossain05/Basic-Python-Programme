score = float(input("Enter your score(a numeric value between 0 and 100): "))

if 0 <= score <= 100 :
    if score < 60 :
        print("Assigned grade: F")
    elif 60 <= score <=69 :
        print("Assigned grade: D")
    elif 70 <= score <=79 :
        print("Assigned grade: C")
    elif 80 <= score <=89 :
        print("Assigned grade: B")
    else :
        print("Assigned grade: A")

else :
    print("Error! The score must be between 0 and 100")