# If you cant give any number 3 times. Program shutting down.
def num_control():
    userInput = input("Please give a number : ")
    count = 1
    while not userInput.isdigit():
        print("Sorry but this is not a number.")
        userInput = input("Please give only a number : ")
        count += 1
        if count == 3 and not userInput.isdigit() :
            print("Sorry but you can't give any number :(" )
            break
    if userInput.isdigit():
        print(f"Congrats. You gave a number at your {count}. trying.")

num_control()
        