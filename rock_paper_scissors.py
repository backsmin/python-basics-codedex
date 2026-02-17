import random

# Instructions:

# Rock beats Scissors.
# Scissors beat Paper.
# Paper beats Rock.
# First, create a player and a computer variable.

# Prompt the player to select number between 1 and 3 with input() and store it in player:
# 1 is for '✊' (Rock) and beats scissors.
# 2 is for '✋' (Paper) and beats rock.
# 3 is for '✌️' (Scissors) and beats paper.
player = int(input('Give me a whole number between 1 and 3. \n 1 is for \'✊\' (Rock) \n 2 is for \'✋\' (Paper) \n 3 is for \'✌️\' (Scissors) \n '))

# Then, use the random.randint() method to assign a number to the computer variable (1 to 3).
computer = random.randint(1, 3)

# Lastly, use control flow to compare the user's choice and the computer's choice,
# determine the winner, and print out who won.

if player == 1 and computer == 3:
    winner = player
    print(f'You won!')

elif player == 1 and computer == 2:
    winner = computer
    print(f'The computer won!')

elif player == 2 and computer == 3:
    winner = computer
    print(f'The computer won!')

elif player == 2 and computer == 1:
    winner = player
    print(f'You won!')

elif player == 3 and computer == 2:
    winner = player
    print(f'You won!')

elif player == 3 and computer == 1:
    winner = computer
    print(f'The computer won!')

else:
    print('It\'s a tie!')
