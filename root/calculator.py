def calculation():
    First = input("Enter First Number And Press Enter : ")
    First = int(First)
    Second = input("Enter Second Number And Press Enter : ")
    Second = int(Second)
    Operator = input("Choose Your Operator And Press Enter : +,*,-,/,% : ")

    if Operator == "+":
        print("Answer Is", First+Second )
    elif Operator == "*":
        print("Answer Is", First*Second)
    elif Operator == "-":
        print("Answer Is", First-Second)
    elif Operator == "/":
        print("Answer Is", First/Second)
    elif Operator == "%":
        print("Answer Is", First%Second)
    else:print("You Type Something Wrong . 🤔")
