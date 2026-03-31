import random

ties = 0
user_score = 0
comp_score = 0
name_1 = input("Enter the name of user: ")
print(f"Wecome {name_1}!!!")
print("Let's play rock, paper, scissors!! \nWinning Rules:")
print("1. Paper vs Rock --> Paper \n2. Rock vs Scissors --> Rock \n 3. Scissors vs Paper --> Scissors")
print("\n")
print("Choices are: \n1. Rock \n2. Paper \n3. Scissors")

while True:
    choice = int(input("Enter your choice from 1-3: "))
    print("\n")
    while choice > 3 or choice < 1:
        choice = int(input("Enter valid input: "))
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else: 
        user_choice = "Scissors"
    print(f"The user's choice is: {user_choice}")
    print("\n")
    computer = random.randint(1,3)
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else: 
        comp_choice = "Scissors"
    print(f"Now computer's choice is: {comp_choice}")
    print("\n")

    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("Paper wins")
        result = "Paper"
    elif ((user_choice == "Scissors" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissors")):
        print("Rock wins")
        result = "Rock"
    elif (user_choice == comp_choice):
        print("It's a tie")
        result = "Tie"
    else:
        print("Scissors wins")
        result = "Scissors"

    if result == "Tie":
        ties +=1
    elif result == user_choice:
        user_score +=1
        print(f"User {name_1} wins")
    else:
        print("Computer wins")
        comp_score +=1

    repeat = input("Do you wanna play again?(yes/no) \n")
    if repeat == "No" or repeat == "NO" or repeat == "no":
        break

print("Score are: ")
print(f"{name_1} score is {user_score} \nComputer's score is {comp_score} \nTies are {ties} ")
print("GAME OVER!!")
print(f"Thank you {name_1} for playing!!")