import random

def determine_winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and bot_choice == 'scissors') or \
         (player_choice == 'scissors' and bot_choice == 'paper') or \
         (player_choice == 'paper' and bot_choice == 'rock'):
        return "You win!"
    else:
        return "Bot wins!"

choices = ['rock', 'paper', 'scissors']

while True:
    player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to end: ").lower()
    if player_choice == 'quit':
        print("Thanks for playing!")
        break
    
    if player_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    bot_choice = random.choice(choices)
    print("Bot chooses:", bot_choice)

    print(determine_winner(player_choice, bot_choice))

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break