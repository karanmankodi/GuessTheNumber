# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import Tkinter


# initialize global variables used in your code
secret_number = random.randint(0,100)
guess = 0
tries = 7
game_mode = 100


# helper function to start and restart the game
def new_game():
    global secret_number
    global guess
    global tries
    guess = 0
    if int(game_mode) == 100:
        secret_number = random.randint(0,100)
        print "The secret number is between 0 & 100 \n"
        tries = 7
        return secret_number
    elif int(game_mode) == 1000:
        secret_number = random.randint(0,1000)
        print "The secret number is between 0 & 1000 \n"
        tries = 10
        return secret_number
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global game_mode
    game_mode = 100
    new_game()
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global game_mode
    game_mode = 1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here    
    global secret_number
    global tries
    
    if (tries > 0):
        if int(guess) > secret_number:
            print "Your guess " +str(int(guess)) +" was higher"
            tries = tries - 1
            print "You have " +str(tries) +" tries left.  \n"
    
        elif int(guess) < secret_number:
            print "Your guess " +str(int(guess)) +" was lower"
            tries = tries - 1
            print "You have " +str(tries) +" tries left. \n"
    
        elif int(guess) == secret_number:
            print "You have guessed the number! \n"
            new_game()
        else:
            print "Invalid input. \n"
    else:
        print "You finished all your tries. Starting new game... \n"
        new_game()
            
    
# create frame
frame = Tkinter.Tk("GuessTheNumber")

# register event handlers for control elements
guessinput = frame.add_input("Your Guess", input_guess, 100)
button100 = frame.add_button("Range of 100", range100, 100)
button1000 = frame.add_button("Range of 1000", range1000, 100)

# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
