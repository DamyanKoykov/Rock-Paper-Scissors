import random

player_input = input("Player can choose from: [r]ock, [p]apaer or [s]cissors: ")  # player input

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
if player_input == "r":
    player_move = rock
elif player_input == "p":
    player_move = paper
elif player_input == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Try again...")

# computer generates random input
computer_input = random.randint(1, 3)
if computer_input == 1:
    computer_move = rock
elif computer_input == 2:
    computer_move = paper
elif computer_input == 3:
    computer_move = scissors

i_win = False
game_draw = False
# draw
if player_input == computer_input:
    game_draw = True
# I win! :)
elif (player_move == rock and computer_input == scissors) or \
        (player_input == paper and computer_input == rock) or \
        (player_move == scissors and computer_move == paper):
    i_win = True
# computer wins :(
else:
    i_win = False

print(f"You chose {player_move}")
print(f"Computer chose {computer_move}")
if game_draw:
    print("Game is draw.")
elif i_win:
    print("Congratulations You Win!!!")
else:
    print("You loose :(")
