p1 = input(print("Choose from rock,paper or scissor: "))
p2 = input(print("Choose from rock,paper or scissor: "))
if p1 == "rock" and p2 == "scissor":
    print("Player 1 wins")
elif p1 == "rock" and p2 == "paper":
    print("Player 2 wins")
elif p1 == "paper" and p2 == "scissor":
    print("Player 2 wins")
elif p1 == "paper" and p2 == "rock":
    print("Player 1 wins")
elif p1 == "scissor" and p2 == "rock":
    print("Player 2 wins")
elif p1 == "scissor" and p2 == "paper":
    print("Player 1 wins")
else:
    print("Please choose from rock,paper or scissor")