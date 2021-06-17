import random
import time
import os

# Variables
player_cards = 26  # Amount of cards the player starts off with
computer_cards = 26  # Amount of cards the computer starts off with
end_loop = False  # Ends the while loop 
round_no = 1
reserve_cards = 0

# Game start
time.sleep(0.2)
while end_loop == False:  # Start prompt
    start = input("Do you want to play the card game 'War'?(y/n)")
    if start == "y":  # If you respond "yes" to "Do you want to play"
        print("OK!")
        end_loop = True
        time.sleep(0.2)
    elif start == "n":  # If you respond "no" to "Do you want to play" + fancy stoping loop
        os.system("cls")
        print("Shuting down")
        time.sleep(0.3)
        os.system("cls")
        print("Shuting down.")
        time.sleep(0.3)
        os.system("cls")
        print("Shuting down..")
        time.sleep(0.3)
        os.system("cls")
        print("Shuting down...")
        time.sleep(0.3)
        exit("Quit")
    else:
        print("That is not a valid answer!")
time.sleep(0.2)

# Game
while player_cards > 0 and computer_cards > 0:  # While the players still has cards
    print("Round:", round_no, ", and you have:", player_cards, "cards left, and the computer has", computer_cards, "cards left, and there are,", reserve_cards, "reserve cards")
    time.sleep(0.2)
    game_sudo_loop = True
    while game_sudo_loop == True:
        sudo_input = input("(Press type 'draw', or enter 'help' to see other commands)")
        if sudo_input == "help":
            print("Use 'sudo add player' to add a cards to the player side, use 'sudo add computer' to add cards to the computer side.")
        elif sudo_input == "sudo add player":
            add = int(input("How many cards do you want to add to the player side (enter a negitive number to subtract)"))
            player_cards = player_cards + add
            print("Added", add, "cards")
            add = 0
            time.sleep(0.5)
        elif sudo_input == "sudo add computer":
            add = int(input("How many cards do you want to add to the computers side (enter a negitive number to subtract)"))
            computer_cards = computer_cards + add
            print("Added", add, "cards")
            add = 0
            time.sleep(0.5)
        elif sudo_input == "draw":
            game_sudo_loop = False
        else:
            print("Invalid input")
            time.sleep(0.2)
    time.sleep(0.2)
    print("You drew a...")
    time.sleep(0.2)
    player_drawn_card = random.randint(1,13)
    if player_drawn_card == 13:
        print("ace!")
    elif player_drawn_card == 12:
        print("king!")
    elif player_drawn_card == 11:
        print("queen!")
    elif player_drawn_card == 10:
        print("jack!")
    else:
        print(player_drawn_card+1,"!")
    time.sleep(0.2)
    print("The computer drew a...")
    computer_drawn_card = random.randint(1,13)
    time.sleep(0.2)
    if computer_drawn_card == 13:
        print("ace!")
    elif computer_drawn_card == 12:
        print("king!")
    elif computer_drawn_card == 11:
        print("queen!")
    elif computer_drawn_card == 10:
        print("jack!")
    else:
        print(computer_drawn_card+1,"!")
    time.sleep(0.2)
    print("That means...")
    time.sleep(0.2)
    if player_drawn_card > computer_drawn_card:
        print("You win!")
        player_cards = player_cards + 1
        player_cards = player_cards + reserve_cards
        computer_cards = computer_cards - 1
        reserve_cards = 0
    elif player_drawn_card == computer_drawn_card:
        print("Its a tie!")
        player_cards = player_cards - 1
        computer_cards = computer_cards -1
        reserve_cards = reserve_cards + 2
    elif player_drawn_card < computer_drawn_card:
        print("You lose!")
        computer_cards = computer_cards + 1
        computer_cards = computer_cards + reserve_cards
        player_cards = player_cards - 1
        reserve_cards = 0
    time.sleep(0.2)
    round_no = round_no + 1
    os.system("cls")
time.sleep(0.2)

# Win section
if player_cards == 0:
    print("You lost!")
    time.sleep(0.2)
    print("The computer won with,", computer_cards, "cards left")
    exit_stat = "Normal ending"
elif computer_cards == 0:
    print("You win!")
    time.sleep(0.2)
    print("You won with,", player_cards, "cards left!")
    exit_stat = "Normal ending"
elif player_cards == computer_cards == 0:
    print("You both lost?")
    time.sleep(0.2)
    print("You both have 0 cards and tied!")
    exit_stat = "Normal ending"
else:
    print("You either broke the game or cheated to get here :P")
    exit_stat = "cheatr"
time.sleep(0.2)
input("Press enter to exit the game...")
exit(exit_stat)