
i = 1
p1Wins = 0
p2Wins = 0
while i <= 3:

    player1 = input("Enter 'R as Rock', 'P as Paper, 'S as Scissors")
    player2 = input("Enter 'R as Rock', 'P as Paper, 'S as Scissors")

   
    if player1 == "R":
        if player2 == "P":
            print("player2 wins")
            p2Wins +=1
        elif player2 == "S":
            print("player1 wins")
            p1Wins +=1
        elif player2 == "R":
            print("Raw")

    if player1 == "P":
        if player2 == "S":
            print("player2 wins")
            p2Wins +=1
        elif player2 == "R":
            print("player1 wins")
            p1Wins += 1
        elif player2 == "P":
            print("Raw")

    if player1 == "S":
        if player2 == "R":
            print("player2 wins")
            p2Wins += 1
        elif player2 == "P":
            print("player1 wins")
            p1Wins += 1
        elif player2 == "S":
            print("Raw")

    i += 1
print("palyer1 wins = ", p1Wins)
print("player2 wins = ", p2Wins)
if p1Wins > p2Wins:
    print("player1 is the winner !!!")
if p1Wins < p2Wins:
    print("player2 is the winner !!!")
if p1Wins == p2Wins:
    print("DRAW !!!")    