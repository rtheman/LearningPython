# Rock-paper-scissors-lizard-Spock template
# Rich Leung | kleung.hkg@gmail.com | https://github.com/rtheman/LearningPython
# 10/19/2013

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

### Global variables:
length = 5		# Length of random number array


# helper functions
def number_to_name(number):
    # fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "ERROR"

   
def name_to_number(name):
    # fill in your code below
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return "error"


def rpsls(name): 
    # convert name to player_number using name_to_number
    player_choice_num = name_to_number(name)
    ##DEBUG## print "Player num = " + str(player_choice_num)
    
    # compute random guess for comp_number using random.randrange()
    comp_choice_num = random.randrange(0, 5)
    ##DEBUG## print "Computer num = " + str(comp_choice_num)
    
    # compute difference of player_number and comp_number modulo five
    if comp_choice_num == ((player_choice_num + 1) % length):
        win_result = "Computer wins!"
    elif comp_choice_num == ((player_choice_num + 2) % length):
        win_result = "Computer wins!"
    elif comp_choice_num == ((player_choice_num - 1) % length):
        win_result = "Player wins!"
    elif comp_choice_num == ((player_choice_num - 2) % length):
        win_result = "Player wins!"
    else:
        win_result = "Both Tied!"
        
    # convert comp_number to name using number_to_name
    player_choice_word = number_to_name(player_choice_num)
    comp_choice_word = number_to_name(comp_choice_num)
    
    # print results
    print 'Player chooses ' + player_choice_word
    print 'Computer chooses ' + comp_choice_word
    print win_result
    print ''
    
    

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


