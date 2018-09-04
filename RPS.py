"""This game called Rock &paper &scissors
   you can play by choosing one of the choices out there and the computer will choice on it's turn, then the game decadice which one is the winner the which one is the loser
   note: the game is the matter of chance
   because the computer choose it's choice randomly
 """
from random import randint

options = ["ROCK","PAPER","SCISSORS"]
message = { 'tie': "Yawn it's a tie",
            'won': "Yay you won!",
            'lost': "Aww you lost!"}

def decide_winner(user_choice, computer_choice):
    """ game called rock, paper, scissors let's play
    Args:
        user_choice : uppercase
        computer_choice: chossen randomly
    Returns:
          choices to detarmine the winner
    """
    print "your choice is %s" % (user_choice)
    print "computer choice is %s" % (computer_choice)
    if user_choice == computer_choice:
      print message['tie']
    elif user_choice == options[0] and computer_choice ==  options[2]:
      print message['won']
    elif user_choice == options[1] and computer_choice ==  options[0]:
      print message['won']
    elif user_choice == options[2] and computer_choice ==  options[1]:
      print message['won']
    else:
      print message['lost']


def confirm_input(user_choice):
    if user_choice == 'ROCK' or 'PAPER' or 'SCISSORS':
        return True
    else:
        return False

def play_RPS():
    user_choice = raw_input("Rock ,Paper or Scissors ? ").upper()
    computer_choice = options[randint(0,2)]
    if confirm_input(user_choice) == True:
        decide_winner(user_choice, computer_choice)
    else:
        print "please enter a valid choice"



play_RPS()  
