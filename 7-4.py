x = ["10", "20", "30", "40"]
while True:
    y = raw_input("type a number")
    if y == "q":
        break
    elif type(y) == int:
        if y in x:
            print("correct")
        else:
            print("incorrect")
    else:
        print("type a number or q.")
        
