from random import randint

t = ["Rock","Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
while player == False:

    player = input("Rock,Paper,Scissors?")
    if player == computer:
        print("TIE!!!")
    elif player == "Rock":
        if computer == "Paper":
            print("YOU LOSE !!!", computer, "covers", player)
        else:
            print("YOU WIN!!!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("YOU LOSE !!!", computer, "cut", player)
        else:
            print("YOU WIN!!!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("YOU LOSE....!!!", computer, "smashes", player)
        else:
            print("YOU WIN!!!", player, "cut", computer)
    else:
        print("That's Not A Valid Play. Check Your Spelling!!")

        player = False
        computer = t[randint(0,2)]

