import random
import time

print('Welcome to my rock paper scissors game!')
input('Press enter to continue...')





def game():
        options = ['rock', 'paper', 'scissors']
        c_score = 0
        score = 0

        def dots():
            for _ in range(3):
                print('.')

                
        def print_score():
            print('Your score is', score, "The computer's score is", c_score)
        while (1==1):
            choice = input('Choose Rock, Paper or Scissors or type "done" to exit: ').lower()
            c_choice = random.choice(options)
                    
            time.sleep(0.3)
            
            if choice == 'done':
                break

            print("Computer chose:", c_choice)
            
            if choice in ['rock', 'r', '1']:
                if c_choice == 'rock':
                    print('Tie!')
                elif c_choice == 'scissors':
                    print('You win!')
                    score += 1
                else:
                    print('Computer wins!')
                    c_score += 1

            elif choice in ['paper', 'p', '2']:
                if c_choice == 'paper':
                    print('Tie!')
                elif c_choice == 'rock':
                    print('You win!')
                    score += 1
                else:
                    print('Computer wins!')
                    c_score += 1

            elif choice in ['scissors', 's', '3']:
                if c_choice == 'scissors':
                    print('Tie!')
                elif c_choice == 'paper':
                    print('You win!')
                    score += 1
                else:
                    print('Computer wins!')
                    c_score += 1

            else:
                print("Invalid choice. Please try again.")
                continue

            dots()
            print_score()


        print('Final score:')
        print('couculating')
        dots()
        if score>c_score:
            print('You won this game, come back for another game')
        elif score<c_score:
             print('Good game, come back next time and you will mabye beat me!')
        else:
            print('Good game we tied, come back for another')
        print_score()

while True:
    new_game=input('do you want to play a game? [Y/N]')
    if new_game in ['Y', 'y']:
        game()
    elif new_game in ['N', 'n']:
        break
    else:
        print('invalid key please type "y" for yes, and "n" for no')
        input('press enter to continue...')
        dots()