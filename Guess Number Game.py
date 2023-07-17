user1 = int(input("Enter the number : "))

i = 1

while i <= 10:
    user2 = int(input("Enter the number you guess : "))
    if user1 < user2:
        print("You entered a bigger number !")
    elif user1 > user2:
        print("You entered a smaller number !")
    else:
        print("You won !!")
        break
    i += 1

if i > 10:
    print("You lost ! ")