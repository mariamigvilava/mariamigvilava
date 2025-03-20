def get_choice(player):
    while True:
        choice = input(f"{player}, enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please try again.")

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
         (choice1 == 'paper' and choice2 == 'rock') or \
         (choice1 == 'scissors' and choice2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Main game loop
while True:
    player1_choice = get_choice("Player 1")
    player2_choice = get_choice("Player 2")
    
    print(f"\nPlayer 1 chose: {player1_choice}")
    print(f"Player 2 chose: {player2_choice}")
    
    result = determine_winner(player1_choice, player2_choice)
    print(result)
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
