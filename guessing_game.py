"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
import random

games_played = []
no_integer = 0

def header(): 
    # On the spirit of randonizing the numbers, header welcome message and 
    #  star position is random.
    print("*"*80)
    
    initial_position_welcome = random.randrange(1,8,1)
    welcome_string = " Welcome to the Guessing Name Game"
    explanation_string = "So simply, so randomly choosen, You will choose a number between 1 and 10"
    
    for i in range(1,9):
        
        left = random.randrange(1,40,5)
        center = random.randrange(1,30)
        right = 80 - (left+center)

        size = left + len(welcome_string) + center + right -30
        string_to_print = "*"*left+ welcome_string+" "*center+"*"*(right-len(welcome_string))
        overflown = 80 - (left+center+len(welcome_string))
        
        if(initial_position_welcome == i):
            if overflown > 0:
                print(string_to_print)
            elif overflown < 0:
                if size >= 80:
                    print("*********** Welcome to the Guessing name ***************************************")
        print("*"*left+" "*center +"*"*right)
        print("*"*80)
    explanation_lenght = int((80 - len(explanation_string))/2)
    print("^"*explanation_lenght+explanation_string+"^"*explanation_lenght)

def validate_float(num):
    # Validate for non-numbers (strings) and then validate for float
    # using the modulo operator
    try:
        num = float(num)
    except ValueError:
        print("Yup, only numbers! (Is '{}' a number?)\n".format(num))
    else:
        num = float(num)
        if num%1 !=  0:
            raise ValueError("No flo flo floating points allowed, must be int int integer\n")
    
        
def validate_range(num):
    # Validate range between 1 and 10
    if(num <= 0 or num >= 11  ):
        raise ValueError("ok, that's a number, but I need it between 1 and 10\n")

def compare(num,secret):
    # Compares the guessed number, as num, to the secret randomized number
    if(num < secret):
        print("Oooopsi, your guess is wrong, you need to get higher\n")
        return True
    elif(num > secret):
        print("You are way to big, the number is little\n")
        return True
    else:
        print("It's a match!, you got it in {} tries\n".format(attempt))
        return False



def generate_number():
    # Generate a random integer between 1 and 10, inclusive
    return(random.randint(1,10))
  
def display_score():
    #display the score for the current player (not global, as wedontknow how)
    # to use files
    highest = 0
    flag = False
    
    for score in games_played:
        current = score
        if flag == True:
            break 
        for i in games_played:
            if i <= current:
                highest = i
                flag = True
    print("\n{} is your Highest Score!".format(highest))
    
            
    
# Start of program Execution
    
header()
player_name = input("\nSo, Youngling, What is your name? ")

super_secret_number = generate_number()

attempt=1
interruption = True
while interruption == True: 
    try:
        number_to_play = input("Lets see if you are lucky, What is the Number? ") 
        validate_float(number_to_play)
    except ValueError as err:
        print("{}".format(err))
    try:
        number_to_play = int(number_to_play)
    except ValueError:
        # no need to print for an integer as float and string test passed,
        no_integer +=1
    else:
        number_to_play = int(number_to_play)
        try:
            validate_range(number_to_play)
        except ValueError as err:
            print("{}".format(err))
        else:
            interruption = compare(number_to_play,super_secret_number)
            if interruption == False:
                games_played.append(attempt)
                continue_playing = input("Would you like to play again (Y/N)? ").lower()
                if(continue_playing == "y"):
                    display_score()
                    interruption = True
                    super_secret_number = generate_number()
                    attempt = 0
                elif(continue_playing == "n"):
                    a = 1
                    for score in games_played:
                        print("On Game {}.- Your Score is: {} ".format(a,score))
                        a+=1
                    print("Thanks for Playing {}, Have a nice day!".format(player_name))
                    interruption = False
                else:
                    # just continue if other than Y/N entered
                    print("Well, that's not Y/N, but let's assume it's a YES!")
                    interruption = True
                    attempt = 0
                    display_score()
                    super_secret_number = generate_number()
                
    attempt+=1