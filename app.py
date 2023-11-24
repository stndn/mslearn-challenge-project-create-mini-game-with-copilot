# write 'hello world' to the console

print('hello world')

# loop until the user decides to quit
# keep track of user's score and number of rounds played

score = 0
rounds_played = 0

while True:
    
    # increment the number of rounds played

    rounds_played += 1

    # get user input that is either 'rock', 'paper', or 'scissors'
    user_input = input('Enter rock, paper, or scissors: ')

    # change user input to lower case

    user_input = user_input.lower()

    # generate a random number between 0 and 2

    import random
    random_number = random.randint(0,2)

    # assign a random choice to the computer

    if random_number == 0:
        computer_choice = 'rock'
    elif random_number == 1:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissors'

    # print the computer's choice

    print('The computer chose', computer_choice)

    # determine who won
    # increase score when user wins
    if user_input == computer_choice:
        print('It\'s a tie!')
    elif user_input == 'rock':
        if computer_choice == 'paper':
            print('You lose!')
        else:
            print('You win!')
            score += 1
    elif user_input == 'paper':
        if computer_choice == 'scissors':
            print('You lose!')
        else:
            print('You win!')
            score += 1
    elif user_input == 'scissors':
        if computer_choice == 'rock':
            print('You lose!')
        else:
            print('You win!')
            score += 1
    else:
        print('Invalid input! You have not entered rock, paper or scissors, try again.')

    # print a message to the console congratulating the winner

    # ask if the user wants to play again

    play_again = input('Play again? (y/n): ')

    # change user input to lower case

    play_again = play_again.lower()

    if play_again == 'n':
        break


# print the final score and number of rounds played

print('Thanks for playing!')
print('Rounds played:', rounds_played)
print('Your score is', score)

